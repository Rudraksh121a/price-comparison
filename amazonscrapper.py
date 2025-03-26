import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import json

def url_for_product(product):
    data={}
    url = f"https://www.amazon.in/s?k={product}"
    
    urlclient = uReq(url)
    amazonpage = urlclient.read()
    bsobj = BeautifulSoup(amazonpage, "html.parser")

    listcontiner=bsobj.find("div", {"class": {"s-main-slot s-result-list s-search-results sg-row"}})
    listitem=listcontiner.find_all("div", {"role": {"listitem"}})
    for i in range(len(listitem)):
        try:
            linkofpage=listitem[i].find("a", {"target": {"_blank"}}).get("href")
          
            name=listitem[i].find("h2").text
           
            image=listitem[i].find("img").get("src")
          
            rating=listitem[i].find("i").text
            
            price=listitem[i].find("span", {"class": {"a-offscreen"}}).text
           
            data[i] = {
            "link": linkofpage,
            "name": name,
            "image": image,
            "rating": rating,
            "price": price
            }
            
            
            
         
        except:
           
            return data
        

def get_product_details(url):
    data={}
    urlclient = uReq(url)
    amazonpage = urlclient.read()
    bsobj = BeautifulSoup(amazonpage, "html.parser")
    aboutItem=bsobj.find("div",{"id":"feature-bullets"}).text 
    customerReview=bsobj.find("div",{"id":"customerReviews"}).find("div",{"id":"product-summary"}).text
    data["aboutItem"]=aboutItem
    data["customerReview"]=customerReview
    return data

     

