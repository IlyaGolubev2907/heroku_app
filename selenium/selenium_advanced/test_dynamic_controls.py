from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_controls(browser, wait):
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")

    remove = browser.find_element(By.XPATH, "//*[text() = 'Remove']")
    remove.click()
    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert message.text == "It's gone!"
    input_field = browser.find_element(By.XPATH, "//input[@type='text']")
    assert not input_field.is_enabled()
    enable = browser.find_element(By.XPATH, "//button[text()='Enable']")
    enable.click()
    enable_message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert enable_message.text == "It's enabled!"
    assert input_field.is_enabled()
