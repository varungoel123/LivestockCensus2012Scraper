# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random
import time
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
path_to_chromedriver = '//home//isb//Downloads//chromedriver'

# run selenium chrome driver (opens a new chrome window)
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
driver.wait = WebDriverWait(driver, 5)	
url = r'http://farmer.gov.in/livestockcensus.aspx'
driver.get(url) # opens the given url
#try:
    #button = driver.wait.until(EC.presence_of_element_located(
#        (By.ID, "ddlstate")))
    #button.click()
#except TimeoutException:
    #print("Box or Button not found in google.com")
#num=1

## create list of all state values by searching for options and values in the state dropdown
stateSelect = Select(driver.find_element_by_id("ddlstate")) 
# stateVal = [] 
# for val in stateSelect.options:
#     stateVal.append(val.get_attribute('value'))

stateVal = {}
for val in stateSelect.options:
    stateVal[val.get_attribute('value')] = val.text
del stateVal['0']

#print(stateVal)
fixed_vars = ["state_code","state_name","district_code","district_name","tehsil-village_name"]
varfilename = "tehsil_column_names.csv"
input_path = r'//home//isb//Documents//nikita//scraping_data//LivestockCensus2012Scraper//'
livestock_vars = pd.read_csv(input_path + varfilename)
#print livestock_vars['exocattle']
columns = fixed_vars + list(livestock_vars.buffaloes) ##for indigenous
col_string = ','.join(columns)
data_all=pd.DataFrame([col_string])


for state in stateVal.keys():
    driver.find_element_by_xpath('//*[@id="ddlstate"]/option[@value=' + state + ']').click()
    # xpath can be obtained by right clicking element in debug mode and copying xpath
    time.sleep(3) # wait for browser
    districtSelect = Select(driver.find_element_by_id("ddldistrict"))
    districtVal = {}
    
    for val in districtSelect.options:
        districtVal[val.get_attribute('value')] = val.text
    del districtVal['0']

    for district in districtVal.keys():
        driver.find_element_by_xpath('//*[@id="ddldistrict"]/option[@value=' + district + ']').click()
        time.sleep(3)
        driver.find_element_by_id("rd_bird").click() 
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlname"]/option[3]').click() #//*[@id="ddlname"]/option[3]//*[@id="ddlname"]/option[3]
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlHouse_non"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddlarea"]/option[2]').click()
        time.sleep(2)
        #driver.find_element_by_xpath('//*[@id="ddlexotic"]/option[2]').click()
        #time.sleep(2)
        driver.find_element_by_id("btnfilter").click()
        time.sleep(10) # important : waits for html to reload
        soup = BeautifulSoup(driver.page_source,"html.parser")
        ## refers to the html part where data is stored
        tag_middlepn14 = soup.find(id="middlepnl4") 
        tag_table = tag_middlepn14.contents[3]
        tag_body = tag_table.contents[1]
        output_path = r'//home//isb//Documents//nikita//scraping_data//LivestockCensus2012Scraper//'
        output_filename = r'data_buff.csv'
        #fixed_valdict = {}
        #tag_table[0]
        fixed_val = state + "," + stateVal[state] +"," +district +"," + districtVal[district] + ","
        for y in range(1,len(tag_body)-1): #ignore first tag as it contains column names
            tag_data = tag_body.contents[y] 
            data_text = tag_data.text # exhume data from the tag
            data_replace = data_text.replace('\n', ',').replace(',,','').replace(' ','') #replace unwanted space, comma and line break
            data_string = fixed_val + data_replace.encode('utf-8') #convert unicode into utf-8 string
            data_list = data_string.split() # convert string into list
            df = pd.DataFrame(data_list) 

            #print len(df.columns) 
            #convert into dataframe
            data_all =data_all.append(df) # append all iterations into final dataframe
            #print len(data_all.columns)   
        data_all.to_csv(output_path + output_filename,index = False, sep='\t', header = False, mode = "a" , header = False, encoding = 'utf-8') # write

      
driver.quit()     
