import shutil
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path


@pytest.fixture
def browser(download_dir):
    options = Options()

    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "download.default_directory": str(download_dir.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "download.restrictions": 0,
        "profile.default_content_settings.popups": 0,
        "browser.download.manager.showWhenStarting": False,
    }

    options.add_experimental_option("prefs", chrome_prefs)

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


@pytest.fixture
def download_dir():
    dir_path = Path(tempfile.mkdtemp())
    yield dir_path
    shutil.rmtree(dir_path)

