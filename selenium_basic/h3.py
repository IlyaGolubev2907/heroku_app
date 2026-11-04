from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
options = select.options
assert len(options) > 0, "Нет опций"

select.select_by_value("1")
assert select.first_selected_option.text == "Option 1", "Выбрана не первая опция"

select.select_by_value("2")
assert select.first_selected_option.text == "Option 2", "Выбрана не вторая опция"

driver.quit()
