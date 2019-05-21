import urllib.request
from bs4 import BeautifulSoup

mainpage = urllib.request.urlopen('https://www.ebay.com/sch/i.html?_nkw=a7+iii&_in_kw=1&_ex_kw=&_sacat=0&_udlo=&_udhi=&LH_Auction=1&LH_ItemCondition=4&LH_Time=1&_ftrt=901&_ftrv=12&_sabdlo=&_sabdhi=&_samilow=&_samihi=&_sadis=15&_stpos=92704-1827&_sargn=-1%26saslc%3D1&_salic=1&_sop=1&_dmd=1&_ipg=50&_fosrp=1')

soup = BeautifulSoup(mainpage, "html.parser")

for items in soup.findAll('li',{"class":"sresult lvresult clearfix li"}):
    header = items.find('a')
    link = header.get('href')
    cond = items.find('div',{"class":"lvsubtitle"})
    price = items.find('span')
    bids = items.find('li',{"class":"lvformat"})

    print(('Link: ') +(link))
    print(('Condition: ') + (cond.text))
    print(('PRICE: ') +(price.text))
    print('Bids: ' + (bids.text))
    print(' ')
    print(' ')