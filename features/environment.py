# environment.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--ignore-certificate-errors") 
    chrome_options.add_argument("--headless=new") 
    context.driver = webdriver.Chrome(options=chrome_options)

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()