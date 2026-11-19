import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.basic
@pytest.mark.smoke
def test_dropdown(browser):
    browser.get("http://the-internet.herokuapp.com/dropdown")

    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    options = select.options
    assert len(options) > 0, "Нет опций"

    select.select_by_value("1")
    assert select.first_selected_option.text == "Option 1", "Выбрана не первая опция"

    select.select_by_value("2")
    assert select.first_selected_option.text == "Option 2", "Выбрана не вторая опция"
