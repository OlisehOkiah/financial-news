import requests
from bs4 import BeautifulSoup
import pandas as pd

News=[]
url="https://finance.yahoo.com/topic/stock-market-news"
r=requests.get(url)
#print(r.status_code)

soup=BeautifulSoup(r.text,'html.parser')
#print(soup)
headlines=soup.find_all('li',class_="js-stream-content Pos(r)")
for i in headlines:
    n=i.text
    News.append(n)

df=pd.DataFrame()
df.to_csv('StockNews.csv')