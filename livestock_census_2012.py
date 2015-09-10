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

data_all=list() #create an empty list
for i in range(len(tag_table)):
    data_text = tag_table[i].text #extract text from the tag 
    data_replace = data_text.replace('\n', ',').replace(',,','') 
    data_string = data_replace.encode() #convert unicode into string
    data_list = data_string.split() # convert string into list
    print data_list
      

    
    


