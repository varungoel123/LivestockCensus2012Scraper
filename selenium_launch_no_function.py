from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random
import time
path_to_chromedriver = './chromedriver'


driver = webdriver.Chrome(executable_path = path_to_chromedriver)
driver.wait = WebDriverWait(driver, 5)	
url = r'http://farmer.gov.in/livestockcensus.aspx'
driver.get(url)
try:
    button = driver.wait.until(EC.presence_of_element_located(
        (By.ID, "ddlstate")))
    #button.click()
except TimeoutException:
    print("Box or Button not found in google.com")

mySelect = Select(driver.find_element_by_id("ddlstate"))
for o in mySelect.options:
    #print o.text + "," + o.value
    print o.text + "," + o.get_attribute('value')
time.sleep(5)
driver.quit()



    #time.sleep(5)
    #driver.quit()