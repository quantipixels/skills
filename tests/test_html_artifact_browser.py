"""Chromium checks for QP mechanics; real upstream rendering is a separate case.

Default transport opens file://, as a user would. QP_TEST_TRANSPORT=content runs
bounded DOM checks where navigation is prohibited, explicitly skipping stronger
navigation evidence. QP_RENDERER_PACKAGES enables the exact-package integration.
"""
import json
import os
import re
import tempfile
import unittest
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'skills/html-artifact/assets'
BASE = (ASSETS / 'base.html').read_text()
CONTENT_ONLY = os.environ.get('QP_TEST_TRANSPORT') == 'content'
GUARD = '''
(() => {
  if (window.__guardInstalled) return;
  window.__guardInstalled = true;
  window.__effects = [];
  for (const method of ['setItem','removeItem','clear']) {
    const original = Storage.prototype[method];
    Storage.prototype[method] = function(...args) { window.__effects.push('storage:'+method); return original.apply(this,args); };
  }
  for (const method of ['pushState','replaceState']) {
    const original = history[method];
    history[method] = function(...args) { window.__effects.push('history:'+method); return original.apply(this,args); };
  }
  const openDB = indexedDB.open.bind(indexedDB);
  indexedDB.open = (...args) => { window.__effects.push('indexedDB'); return openDB(...args); };
  const cookie = Object.getOwnPropertyDescriptor(Document.prototype,'cookie');
  Object.defineProperty(document,'cookie',{get(){return cookie.get.call(document)},set(v){window.__effects.push('cookie');cookie.set.call(document,v)}});
})();
'''


def asset(name):
    return (ASSETS / name).read_text()


def filters():
    return asset('collection-filter-control.html').replace(
        '<!-- Add real data-filter-item elements with declared comma-separated data-filter-values. -->',
        '<article data-filter-item data-filter-values="required">Alpha durable result</article>'
        '<article data-filter-item data-filter-values="required">Beta retry policy</article>'
        '<article data-filter-item data-filter-values="optional">Gamma report</article>')


def carousel():
    return asset('carousel-control.html').replace(
        '<!-- Supply figures with id, data-carousel-item, role=group and aria-label. -->',
        '<figure id="slide-a" data-carousel-item role="group" aria-label="A $&"><p>First</p><label>Value <input value="1"></label></figure>'
        '<figure id="slide-b" data-carousel-item role="group" aria-label="B"><p id="slide-b-detail">Second</p></figure>'
        '<figure id="slide-c" data-carousel-item role="group" aria-label="C"><p>Third</p></figure>')


def diagram(source, identity):
    return f'<figure id="{identity}"><figcaption>Source-supported explanation</figcaption><pre class="mermaid">{source}</pre><div data-diagram-output></div><p data-diagram-status role="status"></p></figure>'


class BrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        executable = os.environ.get('CHROMIUM_PATH')
        if not executable and Path('/usr/bin/chromium').exists():
            executable = '/usr/bin/chromium'
        cls.browser = cls.pw.chromium.launch(executable_path=executable, args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.context = self.browser.new_context(viewport={'width':1280, 'height':900}, color_scheme='light')
        self.context.add_init_script(GUARD)
        self.requests = []
        self.context.on('request', lambda request: self.requests.append(request.url))
        self.context.route(re.compile(r'https?://'), lambda route: route.abort())
        self.page = self.context.new_page()
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))

    def tearDown(self):
        self.context.close()
        self.tmp.cleanup()

    def load(self, content='', connected=False, fragment=''):
        text = BASE.replace('<h1>Artifact title</h1>', '<h1>Control fixture</h1>').replace('</main>', content + '</main>')
        if connected:
            text = text.replace('data-artifact-delivery="portable"', 'data-artifact-delivery="connected"')
        self.document = text
        path = Path(self.tmp.name) / 'test.html'
        path.write_text(text)
        if CONTENT_ONLY:
            self.page.evaluate(GUARD)
            self.page.set_content(text)
        else:
            self.page.goto(path.as_uri() + fragment)

    def assert_no_writes(self):
        self.assertEqual(self.page.evaluate('window.__effects'), [])
        self.assertEqual(self.errors, [])

    def test_view_keyboard_reset(self):
        self.load(asset('view-control.html'))
        expect(self.page.locator('#view-before')).to_be_visible()
        self.page.locator('[data-view-target="view-after"]').focus()
        self.page.keyboard.press('Enter')
        expect(self.page.locator('#view-after')).to_be_visible()
        expect(self.page.locator('#view-before')).to_be_hidden()
        self.page.locator('[data-view-reset]').click()
        expect(self.page.locator('#view-before')).to_be_visible()
        self.assert_no_writes()

    def test_composed_filter_empty_and_reset(self):
        self.load(filters())
        self.page.get_by_role('button', name='Required', exact=True).click()
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(2)
        self.page.locator('[data-filter-search]').fill('beta')
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(1)
        expect(self.page.locator('[data-filter-status]')).to_have_text('Showing 1 of 3 items for Required / beta.')
        self.page.locator('[data-filter-search]').fill('not-present')
        expect(self.page.locator('[data-filter-zero]')).to_be_visible()
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(0)
        self.page.locator('[data-filter-reset]').click()
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(3)
        self.assert_no_writes()

    def test_carousel_input_keys_bounds_literal_label(self):
        self.load(carousel())
        expect(self.page.locator('[data-carousel-live]')).to_have_text('A $&. Item 1 of 3.')
        self.page.locator('input').focus()
        self.page.keyboard.press('ArrowRight')
        expect(self.page.locator('#slide-a')).to_be_visible()
        self.page.locator('[data-carousel]').focus()
        self.page.keyboard.press('ArrowRight')
        expect(self.page.locator('#slide-b')).to_be_visible()
        self.page.keyboard.press('End')
        expect(self.page.locator('[data-carousel-next]')).to_be_disabled()
        self.assertNotIn('#', self.page.url)
        self.assert_no_writes()

    @unittest.skipIf(CONTENT_ONLY, 'Requires actual navigation, not set_content.')
    def test_explicit_nested_fragment_is_navigation(self):
        self.load(carousel(), fragment='#slide-b-detail')
        expect(self.page.locator('#slide-b')).to_be_visible()
        self.page.locator('[data-carousel-next]').click()
        self.assertTrue(self.page.url.endswith('#slide-b-detail'))
        self.assert_no_writes()

    def test_print_preserves_hidden_population(self):
        self.load(asset('view-control.html') + filters() + carousel())
        self.page.get_by_role('button', name='Required', exact=True).click()
        self.page.emulate_media(media='print')
        expect(self.page.locator('[data-view-panel]:visible')).to_have_count(2)
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(3)
        expect(self.page.locator('[data-carousel-item]:visible')).to_have_count(3)
        self.page.emulate_media(media='screen')
        expect(self.page.locator('[data-view-panel]:visible')).to_have_count(1)

    def test_no_javascript_retains_content(self):
        self.load(asset('view-control.html') + filters() + carousel())
        context = self.browser.new_context(java_script_enabled=False)
        try:
            page = context.new_page()
            if CONTENT_ONLY:
                page.set_content(self.document)
            else:
                page.goto(self.page.url)
            expect(page.locator('[data-view-panel]:visible')).to_have_count(2)
            expect(page.locator('[data-filter-item]:visible')).to_have_count(3)
            expect(page.locator('[data-carousel-item]:visible')).to_have_count(3)
            expect(page.locator('[data-view-controls]')).to_be_hidden()
        finally:
            context.close()

    def test_invalid_mapping_preserves_readable_content(self):
        self.load(asset('view-control.html').replace('data-view-target="view-after"', 'data-view-target="missing"'))
        expect(self.page.locator('[data-view-panel]:visible')).to_have_count(2)
        expect(self.page.locator('[data-view-controls]')).to_be_hidden()

    def test_repeated_inclusion_and_nested_ownership(self):
        inner = asset('view-control.html').replace('view-before', 'inner-before').replace('view-after', 'inner-after')
        outer = asset('view-control.html').replace('<p>Replace with the supplied baseline.</p>', inner)
        script = outer[outer.rfind('<script>'):]
        self.load(outer + script)
        self.page.locator('[data-view-target="inner-after"]').click()
        expect(self.page.locator('#inner-after')).to_be_visible()
        expect(self.page.locator('#view-before')).to_be_visible()
        self.page.locator('[data-view-target="view-after"]').click()
        expect(self.page.locator('#view-after')).to_be_visible()
        self.assert_no_writes()

    def test_mobile_theme_and_reduced_motion(self):
        self.load(asset('view-control.html') + filters())
        self.page.set_viewport_size({'width':390, 'height':844})
        self.page.emulate_media(reduced_motion='reduce')
        self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), 390)
        self.page.get_by_role('button', name='Use dark theme').click()
        self.assert_no_writes()

    def test_portable_diagrams_make_no_network_requests(self):
        self.load(diagram('flowchart LR\nA-->B', 'graph') + asset('renderer-control.html'))
        expect(self.page.locator('[data-diagram-status]')).to_contain_text('Portable view')
        expect(self.page.locator('pre.mermaid')).to_be_visible()
        self.assertFalse(any(url.startswith('http') for url in self.requests))
        self.assert_no_writes()

    def test_connected_no_graph_does_not_load_mermaid(self):
        self.load(asset('renderer-control.html'), connected=True)
        expect(self.page.locator('[data-runtime-status]')).to_contain_text('unavailable')
        self.assertFalse(any('mermaid' in url for url in self.requests))

    def test_renderer_network_failure_retains_source(self):
        self.load(diagram('flowchart LR\nA-->B', 'graph') + asset('renderer-control.html'), connected=True)
        expect(self.page.locator('[data-diagram-status]')).to_contain_text('runtime unavailable')
        expect(self.page.locator('pre.mermaid')).to_be_visible()
        self.assert_no_writes()

    @unittest.skipIf(CONTENT_ONLY, 'Intercepted module execution needs a navigation-capable browser.')
    def test_renderer_stub_contract_is_not_real_library_proof(self):
        stub = '''export default {initialize(o){window.__options=o},async render(id,text){if(text.includes('BROKEN'))throw Error('syntax');return {svg:'<svg id="'+id+'" role="img"><title>Stub</title></svg>'}}};'''
        self.context.route('https://cdn.jsdelivr.net/npm/mermaid@12.0.0/dist/mermaid.esm.min.mjs', lambda route: route.fulfill(body=stub, content_type='text/javascript', headers={'Access-Control-Allow-Origin':'*'}))
        self.load(diagram('flowchart LR\nA-->B', 'good') + diagram('BROKEN', 'bad') + asset('renderer-control.html'), connected=True)
        expect(self.page.locator('#good [data-diagram-output] svg')).to_have_count(1)
        expect(self.page.locator('#good pre')).to_be_hidden()
        expect(self.page.locator('#bad pre')).to_be_visible()
        self.assertEqual(self.page.evaluate('window.__options.securityLevel'), 'strict')
        self.assert_no_writes()

    @unittest.skipIf(CONTENT_ONLY, 'Reload cannot be proved with set_content.')
    def test_reload_restores_defaults(self):
        self.load(asset('view-control.html') + filters() + carousel())
        self.page.locator('[data-view-next]').click()
        self.page.locator('[data-filter-search]').fill('beta')
        self.page.locator('[data-carousel-next]').click()
        self.page.get_by_role('button', name='Use dark theme').click()
        self.assert_no_writes()
        self.page.reload()
        expect(self.page.locator('#view-before')).to_be_visible()
        expect(self.page.locator('#slide-a')).to_be_visible()
        expect(self.page.locator('[data-filter-search]')).to_have_value('')
        expect(self.page.locator('[data-filter-item]:visible')).to_have_count(3)
        expect(self.page.get_by_role('button', name='Use dark theme')).to_be_visible()

    @unittest.skipUnless(os.environ.get('QP_RENDERER_PACKAGES') and not CONTENT_ONLY, 'Pinned packages/navigation unavailable; a stub is not a substitute.')
    def test_real_pinned_tailwind_and_mermaid_recipes(self):
        packages = Path(os.environ['QP_RENDERER_PACKAGES']).resolve()
        for package, version in [('@tailwindcss/browser','4.3.3'), ('mermaid','12.0.0')]:
            self.assertEqual(json.loads((packages/package/'package.json').read_text())['version'], version)
        def serve(route):
            for remote, local in [('@tailwindcss/browser@4.3.3/', '@tailwindcss/browser'), ('mermaid@12.0.0/', 'mermaid')]:
                prefix = 'https://cdn.jsdelivr.net/npm/' + remote
                if route.request.url.startswith(prefix):
                    root = (packages/local).resolve()
                    path = (root/route.request.url[len(prefix):].split('?')[0]).resolve()
                    if path.is_relative_to(root) and path.is_file():
                        route.fulfill(path=str(path), content_type='text/javascript', headers={'Access-Control-Allow-Origin':'*'})
                        return
            route.abort()
        self.context.route('https://cdn.jsdelivr.net/**', serve)
        recipes = re.findall(r'```mermaid\n(.*?)\n```', (ROOT/'skills/html-artifact/references/mermaid-recipes.md').read_text(), re.S)
        self.assertEqual(len(recipes), 4)
        self.load('<p id="utility-proof" class="p-6 text-3xl">Utilities</p>' + ''.join(diagram(source, f'graph-{i}') for i,source in enumerate(recipes)) + asset('renderer-control.html'), connected=True)
        expect(self.page.locator('[data-diagram-output] svg')).to_have_count(4, timeout=30000)
        expect(self.page.locator('#utility-proof')).to_have_css('padding-top', '24px', timeout=30000)
        self.assert_no_writes()


if __name__ == '__main__':
    unittest.main()
