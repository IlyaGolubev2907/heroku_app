import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.smoke
def test_checkboxes(browser):
    browser.get("http://the-internet.herokuapp.com/checkboxes")

    checkbox = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    assert len(checkbox) == 2

    assert checkbox[0].is_selected() is False, "Первый чекбокс выбран"
    checkbox[0].click()
    assert checkbox[0].is_selected() is True, "Первый чекбокс не выбран"

    assert checkbox[1].is_selected() is True, "Второй чекбокс не выбран"
    checkbox[1].click()
    assert checkbox[1].is_selected() is False, "Второй чекбокс выбран"

