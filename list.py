import requests, urllib2
from bs4 import BeautifulSoup

#list_page=urllib2.urlopen("https://www.openbugbounty.org/bugbounty-list/page/1/").read()
r=requests.get("https://www.openbugbounty.org/bugbounty-list/page/1")
#print(r.text)

soup=BeautifulSoup(r.text, "html.parser")
print(type(soup))
lists=soup.findAll('tbody')
for lst in lists:
    links=lst.findAll('a')
    print(type(links))
    for i in links:
        print(i.attrs['href'])
# print(lists)
# lst=lists.findAll('a')
#
# print(lst)
