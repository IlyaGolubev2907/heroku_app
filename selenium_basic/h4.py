from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.TAG_NAME, "input")
input.click()

input.send_keys("ABC")
assert input.get_attribute("value") == "", "Буквы ввелись"
input.send_keys("22")
assert input.get_attribute("value") == "22", "Цифры не ввелись"
input.send_keys(Keys.ARROW_UP)
assert input.get_attribute("value") == "23", "Значение не увеличилось"
input.send_keys(Keys.ARROW_DOWN)
assert input.get_attribute("value") == "22", "Значение не уменьшилось"
driver.quit()

