import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.basic
@pytest.mark.smoke

def test_inputs(browser):
    browser.get("http://the-internet.herokuapp.com/inputs")

    input = browser.find_element(By.TAG_NAME, "input")
    input.click()

    input.send_keys("ABC")
    assert input.get_attribute("value") == "", "Буквы ввелись"
    input.send_keys("22")
    assert input.get_attribute("value") == "22", "Цифры не ввелись"
    input.send_keys(Keys.ARROW_UP)
    assert input.get_attribute("value") == "23", "Значение не увеличилось"
    input.send_keys(Keys.ARROW_DOWN)
    assert input.get_attribute("value") == "22", "Значение не уменьшилось"

