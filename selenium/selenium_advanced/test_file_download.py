from selenium.webdriver.common.by import By
import time
from pathlib import Path


def wait_for_download(download_dir: Path, timeout: float = 15.0) -> Path:
    end_time = time.time() + timeout
    while time.time() < end_time:
        files = [
            f for f in download_dir.iterdir()
            if f.is_file() and not f.name.endswith(".crdownload")
        ]
        if files:
            file = files[0]
            size_before = file.stat().st_size
            time.sleep(0.2)
            if file.exists() and file.stat().st_size == size_before and size_before > 0:
                return file
        time.sleep(0.2)
    raise TimeoutError(
    )


def test_file_download(browser, download_dir):
    browser.get("https://the-internet.herokuapp.com/download")
    filename = "some-file.txt"
    browser.find_element(By.LINK_TEXT, filename).click()
    file_path = wait_for_download(download_dir)
    assert file_path.exists()
