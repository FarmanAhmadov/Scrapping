import requests
from bs4 import BeautifulSoup 
import csv
import re

r = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499337.m570.l1313&_nkw=basketball&_sacat=0",timeout = 3).text

soup = BeautifulSoup(r,"lxml")

products = soup.find_all("div",class_="s-item__info clearfix")
p1 = 0
p2 = 0
p3 = 0
p4 = 0

with open("amazon.csv","w") as f:
    csv_writer = csv.writer(f,delimiter = "\t")
    csv_writer.writerow(["Product_ID","Product_Info","Price","Country"])


    for index, item in zip(range(len(products)),products):
        if item ==10:
            break
        try:
            emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
            product_name = item.h3.text
            product_name = emoji_pattern.sub(r"", product_name)

         
        except:
            product_name = None
        try:
            emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
            sec_info = item.find("span",class_ = "SECONDARY_INFO").text
            sec_info = emoji_pattern.sub(r"", sec_info)
            
        except Exception as e:
            sec_info = "--------"
        try:
            price = item.find("span",class_ = "s-item__price").text
            
        except Exception as e:
            price = 0
        try:
            country = item.find("span",class_ = "s-item__location s-item__itemLocation").text.replace("From","").strip()
          
        except Exception as e:
            country = None

        csv_writer.writerow([product_name,sec_info, price, country])
        

    

"""
sec_info = [product.find("span",class_ = "SECONDARY_INFO").text for product in products]

prices = [product.find("span",class_ = "s-item__price").text for product in products]

countries = [product.find("span",class_="s-item__location s-item__itemLocation").text for product in products]"""
"""

    

"""







