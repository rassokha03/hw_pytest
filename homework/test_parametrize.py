"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.fixture(
    scope='function',
    autouse=True,
    params=[(1900, 1200), (1900, 1080), (390, 844), (400, 850)]
)
def browser_settings(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()

@pytest.mark.parametrize('browser_settings',[(1250, 768), (1900, 1080)], indirect= True)
def test_github_desktop(browser_settings):
    browser.open('/')
    browser.element('[href="/login"]').click()
    pass

@pytest.mark.parametrize('browser_settings',[(390, 844), (400, 850)], indirect= True)
def test_github_mobile(browser_settings):
    browser.open('/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()
    pass
