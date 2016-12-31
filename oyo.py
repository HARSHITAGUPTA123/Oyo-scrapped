"""Top oyo rooms in Delhi as present on MOnday,12 Dec 2016 to Tuesday,13 Dec 2016 with 1 guest facility.
"""

from bs4 import BeautifulSoup
import requests
import urllib2
import pandas as pd

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

pages=17

page1='https://www.oyorooms.com/oyos-in-delhi?adults=1&checkin=12%2F12%2F2016&checkout=13%2F12%2F2016&children=0&city=Delhi&country=india&guests=1&location=Delhi%2CIndia&rooms=1&searchType=city&src=undefined'

url1='https://www.oyorooms.com/oyos-in-delhi?adults=1&checkin=12%2F12%2F2016&checkout=13%2F12%2F2016&children=0&city=Delhi&country=india&guests=1&location=Delhi%2CIndia&page='

url3='&rooms=1&searchType=city&src=undefined'



for pageno in range(pages):
     
    
    print pageno+1
    if pageno==0:
        url=page1
    else:
        url=url1+str(pageno+1)+url3
    r=requests.get(url)
    #r=urllib2.urlopen(url)

    soup=BeautifulSoup(r.content,'lxml')
    #print soup.prettify()

    data=soup.find_all('div',{'class':'hotelcard__caption mdl-grid mdl-grid--no-spacing'})

    for item in data:
        
       
        A.append(item.find_all('span',{'class':'hotelcard__details--text hotelcard__details--name'})[0].text)

        B.append(item.find_all('span',{'itemprop':'addressLocality'})[0].text)
        C.append(item.find_all('span',{'itemprop':'addressRegion'})[0].text)
        
        try:
            D.append(item.find_all('span',{'class':'hotelcard__details--disprice'})[0].text.strip())
        except:
            D.append('')
        E.append(item.find_all('span',{'class':'hotelcard__finalPrice'})[0].text.strip())
        
        try:
            F.append(item.find_all('div',{'class':'hotelcard__preappliedDiscount'})[0].text)
        
        except:
            F.append('')
        
        try:
            G.append(item.find_all('span',{'class':'carousal__soldOut-text'})[0].text)
        except:
            G.append('Available')

print len(A),len(B),len(C),len(D),len(E),len(F),len(G)

df=pd.DataFrame(A,columns=['HOTEL NAME'])
df['LOCALITY']=B
df['REGION']=C
df['OLD PRICE']=D
df['PRICE AFTER DISCOUNT']=E
df['% DISCOUNT']=F
df['STATUS']=G

#Saving the dataframe into a csv file
df.to_csv('/home/harshita/web_scrapping/oyorooms.csv',encoding='utf-8')
        
        
