from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC


def test_file_upload(browser, wait):
    browser.get("https://the-internet.herokuapp.com/upload")
    file_path = Path("test_upload.txt").resolve()

    choose_file = browser.find_element(By.ID, "file-upload")
    choose_file.send_keys(str(file_path))
    upload_file = browser.find_element(By.ID, "file-submit")
    upload_file.click()
    uploaded_file = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))
    assert uploaded_file.text == "test_upload.txt"
