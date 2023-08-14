import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Descriprion = []
Reviews = []

for i in range(1, 6):
    url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" +str(i)
    r = requests.get(url)
    # print(r)

    
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")


    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
    # print(len(Product_name))
    print(Product_name)


    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    # print(len(Prices))
    print(Prices)


    Desc = box.find_all("ul", class_="_1xgFaf")
    for i in Desc:
        name = i.text
        Descriprion.append(name)
    # print(len(Descriprion))
    print(Descriprion)


    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
        name = i.text
        Reviews.append(name)
    # print(len(Reviews))
    print(Reviews)


    df = pd.DataFrame({"Names": Product_name, "Prices": Prices,"Description": Descriprion, "Reviews": Reviews})
    print(df)

    df.to_csv("D:/python/flipkart.com iphone.csv")