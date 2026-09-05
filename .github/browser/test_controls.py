"""Exercise shipped HTML controls, not substitute implementations."""
import os
from pathlib import Path
import re
import unittest

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / 'skills/productivity/html-artifact/assets'


def asset(name):
    return re.sub(r'<!--.*?-->', '', (ASSETS / name).read_text(encoding='utf-8'), flags=re.S)


def carousel(identity):
    body = asset('carousel-control.html')
    body = body.replace('data-carousel\n', f'id="{identity}" data-carousel\n', 1)
    items = ''.join(f'<figure id="{identity}-{n}" data-carousel-item role="group" aria-label="Item {n}"><p>Content {n}</p></figure>' for n in range(1, 4))
    return body.replace('<div data-carousel-track>', '<div data-carousel-track>' + items)


def filtered(identity):
    body = asset('collection-filter-control.html')
    body = body.replace('data-collection-filter\n', f'id="{identity}" data-collection-filter\n', 1)
    buttons = ''.join(f'<button type="button" data-filter-control data-filter-value="{key}" aria-pressed="false">{key}</button>' for key in ('alpha', 'beta', 'none'))
    body = body.replace('>All</button>', '>All</button>' + buttons)
    return body.replace('<div data-filter-items>', '<div data-filter-items><article data-filter-item data-filter-values="alpha">Alpha</article><article data-filter-item data-filter-values="beta">Beta</article>')


def fixture():
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Control proof</title><style>'
            + (ASSETS / 'visual-foundation.css').read_text() + '</style></head><body>'
            + '<header id="artifact-top" data-back-to-top-target tabindex="-1"><h1>Control proof</h1></header>'
            + asset('theme-control.html') + carousel('one') + carousel('two')
            + filtered('first') + filtered('second')
            + '<details id="closed" data-print-expand><summary>Evidence</summary><p id="deep">Visible evidence</p></details>'
            + '<details id="already-open" data-print-expand open><summary>Open evidence</summary><p>Retained</p></details>'
            + asset('report-control.html') + asset('back-to-top-control.html') + '</body></html>')


class ControlBrowserProof(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        executable = os.environ.get('CHROMIUM_EXECUTABLE')
        cls.browser = cls.playwright.chromium.launch(executable_path=executable, headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def open_fixture(self, javascript=True, narrow=False):
        context = self.browser.new_context(java_script_enabled=javascript, viewport={'width': 390 if narrow else 1100, 'height': 800}, reduced_motion='reduce')
        self.addCleanup(context.close)
        page = context.new_page()
        errors, requests = [], []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('request', lambda request: requests.append(request.url))
        # DOM/interaction proof on exact inline bytes; URL transport is a
        # separate claim. This works without granting browser network access.
        page.set_content(fixture())
        self.addCleanup(lambda: self.assertEqual(errors, []))
        self.addCleanup(lambda: self.assertEqual(requests, []))
        return page

    def test_javascript_off_keeps_content_and_native_navigation(self):
        page = self.open_fixture(javascript=False)
        expect(page.locator('[data-carousel-item]:visible')).to_have_count(6)
        expect(page.locator('[data-filter-item]:visible')).to_have_count(4)
        expect(page.locator('[data-carousel-controls]:visible')).to_have_count(0)
        expect(page.locator('[data-filter-controls]:visible')).to_have_count(0)
        expect(page.locator('[data-theme-toggle]')).to_be_hidden()
        page.locator('[data-back-to-top]').click()
        self.assertTrue(page.url.endswith('#artifact-top'))

    def test_theme_keyboard_and_system_override(self):
        page = self.open_fixture()
        page.emulate_media(color_scheme='dark')
        expect(page.locator('html')).to_have_attribute('data-theme', 'dark')
        control = page.locator('[data-theme-toggle]')
        control.focus()
        page.keyboard.press('Enter')
        expect(page.locator('html')).to_have_attribute('data-theme', 'light')
        page.emulate_media(color_scheme='light')
        page.emulate_media(color_scheme='dark')
        expect(page.locator('html')).to_have_attribute('data-theme', 'light')
        expect(control).to_have_attribute('title', 'Use dark theme')

    def test_carousel_keyboard_bounds_hash_and_instances(self):
        page = self.open_fixture(narrow=True)
        first = page.locator('#one')
        first.focus()
        page.keyboard.press('ArrowRight')
        expect(page.locator('#one-2')).to_be_visible()
        expect(page.locator('#two-1')).to_be_visible()
        self.assertTrue(page.url.endswith('#one-2'))
        first.focus()
        page.keyboard.press('End')
        expect(first.locator('[data-carousel-next]')).to_be_disabled()
        page.keyboard.press('Home')
        expect(first.locator('[data-carousel-previous]')).to_be_disabled()
        page.evaluate("location.hash = 'two-3'")
        expect(page.locator('#two-3')).to_be_visible()

    def test_filter_counts_zero_and_instances(self):
        page = self.open_fixture(narrow=True)
        first = page.locator('#first')
        first.get_by_role('button', name='alpha', exact=True).click()
        expect(first.locator('[data-filter-item]:visible')).to_have_count(1)
        expect(page.locator('#second [data-filter-item]:visible')).to_have_count(2)
        expect(first.locator('[data-filter-status]')).to_have_text('Showing 1 of 2 items for alpha.')
        first.get_by_role('button', name='none', exact=True).click()
        expect(first.locator('[data-filter-zero]')).to_be_visible()
        expect(first.locator('[data-filter-item]:visible')).to_have_count(0)
        first.get_by_role('button', name='All', exact=True).click()
        expect(first.locator('[data-filter-item]:visible')).to_have_count(2)

    def test_report_reveals_deep_link_and_restores_print_state(self):
        page = self.open_fixture()
        page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
        expect(page.locator('#closed')).to_have_attribute('open', '')
        page.evaluate("window.dispatchEvent(new Event('afterprint'))")
        self.assertFalse(page.locator('#closed').evaluate('(node) => node.open'))
        self.assertTrue(page.locator('#already-open').evaluate('(node) => node.open'))
        page.evaluate("location.hash = 'deep'")
        expect(page.locator('#closed')).to_have_attribute('open', '')
        page.locator('[data-back-to-top]').focus()
        page.keyboard.press('Enter')
        expect(page.locator('#artifact-top')).to_be_focused()


if __name__ == '__main__':
    unittest.main()
