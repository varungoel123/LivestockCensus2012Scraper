from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random
import time
path_to_chromedriver = './chromedriver'

def init_driver():
	driver = webdriver.Chrome(executable_path = path_to_chromedriver)
	driver.wait = WebDriverWait(driver, 5)
	return driver

url = r'http://farmer.gov.in/livestockcensus.aspx'

def lookup(driver, query):
    driver.get(url)
    try:
        button = driver.wait.until(EC.presence_of_element_located(
            (By.ID, "ddlstate")))
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")

if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    #time.sleep(5)
    #driver.quit()

