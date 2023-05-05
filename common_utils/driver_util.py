import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    chrome_version = os.getenv("CHROME_VERSION", "latest")
    firefox_version = os.getenv("FIREFOX_VERSION", "latest")

    if browser == "chrome":
        return webdriver.Chrome(executable_path=ChromeDriverManager(version=chrome_version).install())
    elif browser == "firefox":
        return webdriver.Firefox(executable_path=GeckoDriverManager(version=firefox_version).install())
    else:
        raise ValueError(f"Unsupported browser: {browser}")