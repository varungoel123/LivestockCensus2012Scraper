## read html from the URL
import urllib2
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series

url = "http://farmer.gov.in/livestockcensus.aspx"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
tag_middlepn14 = soup.find(id="middlepnl4") 
tag_table = tag_middlepn14.contents[3]
tag_body = tag_table.contents[1]

output_path ='C:\\Users\\malaniaayushi\\Desktop\\'
output_filename = 'final_data.csv'
data_all=pd.DataFrame() #create an empty dataframe
#range from second tag to the last tag which contains data
for y in range(1,len(tag_body)-1): #ignore first tag as it contains column names
    tag_data = tag_body.contents[y] 
    data_text = tag_data.text # exhume data from the tag
    data_replace = data_text.replace('\n', ',').replace(',,','').replace(' ','') #replace unwanted space, comma and line break
    data_string = data_replace.encode() #convert unicode into string
    data_list = data_string.split() # convert string into list
    df = pd.DataFrame(data_list) #convert into dataframe
    data_all =data_all.append(df) # append all iterations into final dataframe

data_all.to_csv(output_path + output_filename, header=False, index = False, sep='\t') # write data into csv file
 
    
    


