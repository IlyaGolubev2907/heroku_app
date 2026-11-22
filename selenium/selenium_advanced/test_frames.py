from selenium.webdriver.common.by import By


def test_file_frames(browser, wait):
    browser.get("https://the-internet.herokuapp.com/frames")

    iframe_button = browser.find_element(By.CSS_SELECTOR, "a[href='/iframe']")
    iframe_button.click()
    iframe = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe)
    text = browser.find_element(By.ID, "tinymce")
    assert text.text == "Your content goes here."
