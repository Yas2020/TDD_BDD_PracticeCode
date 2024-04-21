"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')


def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Instantiate the Chrome WebDriver
    # options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument("--no-sandbox") # Bypass OS security model
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.google.com")
        print("Page title was '{}'".format(driver.title))
    finally:
        driver.quit()
    # context.driver = webdriver.Chrome(options=options)
    # context.driver.implicitly_wait(context.wait_seconds)

def after_all(context):
    """ Executed after all tests """
    # context.driver.quit()


