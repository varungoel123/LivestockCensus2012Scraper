## read html from the URL
import urllib2
import requests
from bs4 import BeautifulSoup

url = "http://farmer.gov.in/livestockcensus.aspx"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
## refers to the html part where data is stored
tag_table = soup.find_all("table", style="text-align: left; width: 100%;" )

#tag_table[0]
import pandas as pd
from pandas import DataFrame, Series
data_all=pd.DataFrame()
for i in range(0,len(tag_table)):
    data_text = tag_table[i].text #extract text from the tag 
    data_replace = data_text.replace('\n', ',').replace(',,','').replace(' ','')
    data_string = data_replace.encode() #convert unicode into string
    data_list = data_string.split() # convert string into list
    df = pd.DataFrame(data_list) #convert into dataframe
    data_all =data_all.append(df) # append all iterations into final dataframe
    #print data_all
data_all.to_csv('C:\\Users\\malaniaayushi\\Desktop\\data.csv', index = False, sep='\t') #read 
      

    
    


