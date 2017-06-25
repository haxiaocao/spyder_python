from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.chrome()
driver.get('http://quote.eastmoney.com/zs000001.html')

html = driver.page_source
soup = BeautifulSoup(html)

cont=soup.find('div',{"id":"qqgscont"})
print cont

# check out the docs for the kinds of things you can do with 'find_all'
# this (untested) snippet should find tags with a specific class ID
# see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
#for tag in soup.find_all("a", class_="my_class"):
#    print tag.text
