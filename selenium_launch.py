from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time
path_to_chromedriver = './chromedriver'

def init_driver():
	driver = webdriver.Chrome(executable_path = path_to_chromedriver)
	driver.wait = WebDriverWait(driver, 5)
	return driver

url = r'http://farmer.gov.in/livestockcensus.aspx'

driver = init_driver()
driver.get(url)