"""Browser proof for the built artifact: native file delivery and failure fallback."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parents[2]
RENDERER = REPO / 'skills/productivity/html-artifact/scripts/graph/render.mjs'


class GraphArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.directory = Path(cls.temp.name)
        cls.document = cls.directory / 'relationships.html'
        source = cls.directory / 'relationships.json'
        source.write_text(json.dumps({
            'title': 'Service relationships', 'summary': 'One supplied dependency.', 'directed': True,
            'source': {'label': 'Design fixture', 'href': 'https://example.test/design'},
            'elements': [{'data': {'id': 'api', 'label': 'API'}}, {'data': {'id': 'db', 'label': 'Database'}},
                         {'data': {'id': 'write', 'label': 'writes', 'source': 'api', 'target': 'db'}}]
        }), encoding='utf-8')
        result = subprocess.run(['node', str(RENDERER), '--input', str(source)], capture_output=True, check=True)
        cls.document.write_bytes(result.stdout)
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.temp.cleanup()

    def page(self, **options):
        context = self.browser.new_context(**options)
        self.addCleanup(context.close)
        return context.new_page()

    def test_file_delivery_selection_keyboard_zoom_theme_and_offline(self):
        page = self.page(viewport={'width': 390, 'height': 844}, reduced_motion='reduce')
        requests, errors = [], []
        page.on('request', lambda request: requests.append(request.url) if request.url.startswith(('http:', 'https:')) else None)
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(self.document.as_uri())
        page.locator('[data-qp-graph][data-ready="true"]').wait_for()
        self.assertGreater(page.locator('[data-graph-view] canvas').count(), 0)
        page.get_by_label('Select a node').select_option('db')
        self.assertIn('Selected Database', page.locator('[data-graph-status]').inner_text())
        page.get_by_role('button', name='Zoom in', exact=True).focus()
        page.keyboard.press('Enter')
        self.assertIn('Zoom ', page.locator('[data-graph-status]').inner_text())
        page.get_by_role('button', name='Fit graph', exact=True).click()
        self.assertIn('2 nodes, 1 relationships', page.locator('[data-graph-status]').inner_text())
        original = page.locator('html').get_attribute('data-theme')
        page.locator('[data-theme-toggle]').click()
        self.assertNotEqual(page.locator('html').get_attribute('data-theme'), original)
        self.assertTrue(page.get_by_text('API → Database: writes', exact=False).is_visible())
        self.assertTrue(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'))
        self.assertEqual(requests, [])
        self.assertEqual(errors, [])

    def test_no_javascript_retains_all_supplied_meaning(self):
        page = self.page(java_script_enabled=False)
        page.goto(self.document.as_uri())
        self.assertTrue(page.get_by_role('heading', name='Service relationships').is_visible())
        self.assertTrue(page.get_by_text('API → Database: writes', exact=False).is_visible())
        self.assertTrue(page.get_by_role('link', name='Design fixture').is_visible())
        self.assertTrue(page.locator('[data-graph-controls]').is_hidden())
        self.assertTrue(page.locator('[data-graph-view]').is_hidden())

    def test_renderer_failure_keeps_text_and_discloses_unavailability(self):
        page = self.page()
        page.add_init_script("HTMLCanvasElement.prototype.getContext = function () { throw new Error('fixture renderer unavailable'); };")
        page.goto(self.document.as_uri())
        page.locator('[data-qp-graph][data-ready="unavailable"]').wait_for()
        self.assertTrue(page.get_by_text('API → Database: writes', exact=False).is_visible())
        self.assertIn('Interactive view unavailable', page.locator('[data-graph-status]').inner_text())
        self.assertTrue(page.locator('[data-graph-controls]').is_hidden())
        self.assertTrue(page.locator('[data-graph-view]').is_hidden())


if __name__ == '__main__':
    unittest.main()
