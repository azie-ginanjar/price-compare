from bs4 import BeautifulSoup as bs
from urllib2 import urlopen

blFile = urlopen("https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_organic&search%5Bkeywords%5D=hotwheels")
blHtml = blFile.read()
blFile.close()


soup = bs(blHtml, "html.parser")

blAll = soup.find_all("div", class_="basic-products basic-products--grid")
for div in blAll:
    for innerDiv in div.find_all("div", class_="product-card"):
        for inner2Div in innerDiv.find_all("div", class_="product-media"):
            for anchor in inner2Div.find_all("a"):
                print(anchor.get("href"))