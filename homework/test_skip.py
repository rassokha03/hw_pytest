"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

def mobile(width):
    return width < 1200
@pytest.fixture(params=[(1200, 1900), (600, 900), (850, 400)])
def browser_settings(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    pass


def test_github_desktop(browser_settings):
    if mobile(browser.config.window_width):
        pytest.skip('Этот тест для мобильных устройств')
    browser.open('/')
    browser.element('[href="/login"]').click()
    pass


def test_github_mobile(browser_settings):
    if  not mobile(browser.config.window_width):
        pytest.skip('Этот тест для десктопных устройств')
    browser.open('/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()
    pass
