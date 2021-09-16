import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language',action='store',default='en',help='Choose language.Example en, ru, fr...')


@pytest.fixture(scope='function')
def browser(request):
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print('\nbrowser quit')
    browser.quit()
    