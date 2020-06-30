import requests, urllib2
from bs4 import BeautifulSoup

#program_page=urllib2.urlopen("https://www.openbugbounty.org/bugbounty/GordonChanNet/").read()
r=requests.get("https://www.openbugbounty.org/bugbounty/loswebosde/")

soup=BeautifulSoup(r.text, "html.parser")
lst=soup.find('form', method="POST")

print("Scopes:")
scope=lst.findAll('td', style="text-align:center; border:0; vertical-align: middle;border-bottom: 1px solid #ddd;")
for i in scope:
    ln=str(i).split(">")[1].split("<")[0]
    print(ln)
print('\n')
awards=str(lst).split("Possible Awards:")[1].split("</p>")[1].replace('\n', '').replace('<p>', '')
print("Awards:")
print(awards)
