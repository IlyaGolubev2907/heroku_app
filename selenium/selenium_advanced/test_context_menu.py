from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_context_menu(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")

    actions = ActionChains(browser)
    context_menu = browser.find_element(By.ID, "hot-spot")
    actions.context_click(context_menu).perform()
    alert = browser.switch_to.alert
    assert alert.text == "You selected a context menu"
    alert.dismiss()
