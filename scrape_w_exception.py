## ----coding: utf-8-----
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random
import time
import re
import string
import urlparse
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
path_to_chromedriver = './chromedriver'

#run selenium chrome driver (opens a new chrome window)
#driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://farmer.gov.in/livestockcensus.aspx'
driver = webdriver.PhantomJS()
#driver.set_window_size(1120, 550)
driver.get(url) 
driver.wait = WebDriverWait(driver, 5)	

# opens the given url

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

print(stateVal)
fixed_vars = ["state_code","state_name","district_code","district_name","tehsil-village_name"]
varfilename = "tehsil_column_names.csv"
input_path = r'./'
livestock_vars = pd.read_csv(input_path + varfilename)
print livestock_vars['exocattle']
columns = fixed_vars + list(livestock_vars.exocattle)
col_string = ','.join(columns)

check_scrape = pd.read_csv("./scraped_data.csv")
dist_scraped = pd.unique(check_scrape.district_code)
dist_scraped = dist_scraped.astype(int)
dist_scraped = dist_scraped.astype(str)

i=0
for d in dist_scraped:
    #print len(d)
    if len(d) <=2:
        d = '0'*(3-len(d)) + d
        dist_scraped[i] = d
    i+=1

#print len(check_scrape.columns)



#l = "491"
#print (l in dist_scraped)
for state in stateVal.keys():
    driver.find_element_by_xpath('//*[@id="ddlstate"]/option[@value=' + state + ']').click()
    # xpath can be obtained by right clicking element in debug mode and copying xpath
    time.sleep(5) # wait for browser
    districtSelect = Select(driver.find_element_by_id("ddldistrict"))
    districtVal = {}
    
    for val in districtSelect.options:
        districtVal[val.get_attribute('value')] = val.text
    del districtVal['0']

    for district in districtVal.keys():
        if district in dist_scraped:
            continue
        print district + ","+ districtVal[district]
        data_all =pd.DataFrame()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ddldistrict"]/option[@value=' + district + ']').click()
        time.sleep(3)
        try:
            anim_clk = driver.wait.until(EC.element_to_be_clickable(
            (By.ID, "rd_animal")))
            anim_clk.click()
        except TimeoutException:
            #driver.quit()
            print("Box or Button not found")    
        #driver.find_element_by_id("rd_animal").click()
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
        #try:
            #load_results=driver.wait.until(EC.presence_of_element_located(
            #(By.ID, "dlist_Cattle_E")))
        time.sleep(6) # important : waits for html to reload
        soup = BeautifulSoup(driver.page_source,"html.parser")
        ## refers to the html part where data is stored
        tag_middlepn14 = soup.find(id="middlepnl4") 
        tag_table = tag_middlepn14.contents[3]
        tag_body = tag_table.contents[1]
        output_path = r'./'
        output_filename = r'scraped_data.csv'
        #fixed_valdict = {}
        #tag_table[0]
        fixed_val = state + "," + stateVal[state] +"," +district +"," + districtVal[district] + ","
        for y in range(1,len(tag_body)-1): #ignore first tag as it contains column names
            tag_data = tag_body.contents[y]
            #print(tag_data) 
            data_text = tag_data.text.replace(',','') # exhume data from the tag
            data_replace = data_text.replace('\n', ',').replace(',,','').replace(' ','') #replace unwanted space, comma and line break
            #print(data_replace)
            fixed_val = fixed_val.replace('\n', ',').replace(',,','').replace(' ','') #replace unwanted space, comma and line break
            #data_string = fixed_val + data_replace.decode('utf-8') #convert unicode into utf-8 string
            #print(data_string)
            data_list = data_string.split() # convert string into list
            df = pd.DataFrame(data_list) 
            #print df
            #print len(df.columns) 
            #convert into dataframe
            data_all =data_all.append(df) # append all iterations into final dataframe
            #print len(data_all.columns)   
        #data_all.to_csv(output_path + output_filename,index = False, sep='\t', header = False, mode = "a")
        print(district)
             
        #except TimeoutException:
            #driver.quit()
            #print("Box or Button not found")      

            




