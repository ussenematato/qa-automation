import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture
def browser():
    firefox_binary = (
        "/snap/firefox/current/usr/lib/firefox/firefox"
        if __import__("pathlib").Path("/snap/firefox/current/usr/lib/firefox/firefox").exists()
        else shutil.which("firefox")
    )
    geckodriver_path = shutil.which("geckodriver")

    if not firefox_binary:
        raise RuntimeError("Firefox não encontrado no ambiente.")
    if not geckodriver_path:
        raise RuntimeError("geckodriver não encontrado no ambiente.")

    options = FirefoxOptions()
    options.binary_location = firefox_binary
    options.add_argument("--headless")
    options.add_argument("--window-size=1280,1024")

    driver = webdriver.Firefox(
        service=FirefoxService(executable_path=geckodriver_path),
        options=options,
    )
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
