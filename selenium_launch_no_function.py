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
#try:
    #button = driver.wait.until(EC.presence_of_element_located(
#        (By.ID, "ddlstate")))
    #button.click()
#except TimeoutException:
    #print("Box or Button not found in google.com")
#num=1
stateSelect = Select(driver.find_element_by_id("ddlstate"))
stateVal = []
for val in stateSelect.options:
    stateVal.append(val.get_attribute('value'))

print stateVal



for val in stateSelect.options:
    stateVal.append(val.get_attribute('value'))
for state in stateVal[1:]:
    driver.find_element_by_xpath('//*[@id="ddlstate"]/option[@value=' + state + ']').click()
    time.sleep(5)
    districtSelect = Select(driver.find_element_by_id("ddldistrict"))
    districtVal = []
    for val in districtSelect.options:
        districtVal.append(val.get_attribute('value'))
    for district in districtVal[1:]:
        driver.find_element_by_xpath('//*[@id="ddldistrict"]/option[@value=' + district + ']').click()
        time.sleep(3)
        driver.find_element_by_id("rd_animal").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlname"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlHouse_non"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlarea"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlexotic"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_id("btnfilter").click()
        time.sleep(30)
driver.quit()