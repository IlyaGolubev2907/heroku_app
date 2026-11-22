import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.basic
@pytest.mark.smoke
def test_dropdown(browser):
    browser.get("http://the-internet.herokuapp.com/dropdown")

    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    actual_options = [option.text for option in select.options]
    expected_options = ["Please select an option", "Option 1", "Option 2"]
    assert actual_options == expected_options, f"Ожидались опции {expected_options}, но получены {actual_options}"

    select.select_by_value("1")
    assert select.first_selected_option.text == "Option 1", "Выбрана не первая опция"

    select.select_by_value("2")
    assert select.first_selected_option.text == "Option 2", "Выбрана не вторая опция"
