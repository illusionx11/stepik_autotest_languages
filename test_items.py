import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture
def language(request):
    return request.config.getoption("language")

def test_add_to_basket_button(browser: webdriver.Chrome, language: str):
    
    language_maps = {
            "ru": "Добавить в корзину",
            "en-gb": "Add to basket",
            "es": "Añadir al carrito",
            "fr": "Ajouter au panier"
        }
        
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    try:
        browser.get(url)
        
        time.sleep(30)
        add_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        add_button_text = add_button.text
        assert add_button_text == language_maps[language], f"Wrong button text: Expected '{language_maps[language]}', got '{add_button_text}'"
    
    except NoSuchElementException:
        pytest.fail("Requested page doesn't have add to basket button")
    
    
    