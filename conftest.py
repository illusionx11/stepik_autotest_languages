import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ACCEPTED_LANGUAGES = ["ru", "en-gb", "es", "fr"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help=f"Choose language [{'/'.join(ACCEPTED_LANGUAGES)}]")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    
    if language in ACCEPTED_LANGUAGES:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstarting chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        
    else:
        raise pytest.UsageError(f"--language should be one of the following: [{'/'.join(ACCEPTED_LANGUAGES)}]")
    
    yield browser
    
    print("\nquitting browser..")
    browser.quit()