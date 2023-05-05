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
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    
    if browser == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        return webdriver.Chrome(executable_path=ChromeDriverManager(version=chrome_version).install(), options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        return webdriver.Firefox(executable_path=GeckoDriverManager(version=firefox_version).install(), options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")