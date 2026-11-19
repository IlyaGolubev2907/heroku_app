from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/typos")

count = 1
max_count = 10
correct_text = "Sometimes you'll see a typo, other times you won't."

text = driver.find_element(By.TAG_NAME, "p")

while count < max_count:
    p = driver.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
    shown_text = p.text.strip()
    if shown_text != correct_text:
        print(f"Опечатка найдена с попытки {count}: {shown_text}")
        break
    driver.refresh()
    count += 1

assert count < max_count, f"Опечатка не найдена за {max_count} попыток"
driver.quit()