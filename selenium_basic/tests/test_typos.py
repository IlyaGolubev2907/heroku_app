import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.advanced
@pytest.mark.regression
def test_detect_typo(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    count = 1
    max_count = 10
    correct_text = "Sometimes you'll see a typo, other times you won't."

    text = browser.find_element(By.TAG_NAME, "p")

    while count < max_count:
        p = browser.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
        shown_text = p.text.strip()
        if shown_text != correct_text:
            print(f"Опечатка найдена с попытки {count}: {shown_text}")
            break
        browser.refresh()
        count += 1

    assert count < max_count, f"Опечатка не найдена за {max_count} попыток"