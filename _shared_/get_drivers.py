from webdrivermanager import GeckoDriverManager, ChromeDriverManager
from selenium import webdriver


def download_drivers():
    # Download firefox driver and add it to the environment variable if it's not already there!
    gdd = GeckoDriverManager()
    gdd.download_and_install()
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")

    # Download chrome driver and add it to the environment variable if it's not already there!
    c = ChromeDriverManager()
    c.download_and_install()
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
