"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture
def from_desktop():
    browser.config.window_width = 1900
    browser.config.window_height = 1200
    browser.config.base_url = 'https://github.com/'


@pytest.fixture
def from_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.config.base_url = 'https://github.com/'

def test_github_desktop(from_desktop):
    browser.open('/')
    browser.element('[href="/login"]').click()


def test_github_mobile(from_mobile):
    browser.open('/')
    browser.element('[class*="rounded my-1"]').click()
    browser.element('[href="/login"]').click()
