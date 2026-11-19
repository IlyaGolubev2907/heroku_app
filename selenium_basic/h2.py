from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
assert len(checkbox) == 2

assert checkbox[0].is_selected() is False, "Первый чекбокс выбран"
checkbox[0].click()
assert checkbox[0].is_selected() is True, "Первый чекбокс не выбран"

assert checkbox[1].is_selected() is True, "Второй чекбокс не выбран"
checkbox[1].click()
assert checkbox[1].is_selected() is False, "Второй чекбокс выбран"
driver.quit()
