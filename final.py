import requests, urllib2
from bs4 import BeautifulSoup

json_out=open("json.txt","a")

def program_details(link):
    full_link=("https://www.openbugbounty.org"+link)
    r=requests.get(full_link)

    soup=BeautifulSoup(r.text, "html.parser")
    lst=soup.find('form', method="POST")
    print("Link: "+full_link+"\n")
    print("Scopes:")
    scope=lst.findAll('td', style="text-align:center; border:0; vertical-align: middle;border-bottom: 1px solid #ddd;")
    scope_list=[]
    for i in scope:
        ln=str(i).split(">")[1].split("<")[0]
        print(ln)
        scope_list.append(ln)

    awards=str(lst).split("Possible Awards:")[1].split("</p>")[1].replace('\n', '').replace('<p>', '').replace('</br>', '').replace('<br>', '').replace('<br/>', '')
    print("\nAwards:")
    print(awards)
    print("--------------------------------------------")
    json_out.write("{\"Link\":\""+full_link+"\",\"Scopes\":\""+(','.join(scope_list))+"\",\"Reward\":\""+awards+"\"}"+"\n")

for i in range(1,30):
    r=requests.get("https://www.openbugbounty.org/bugbounty-list/page/"+str(i))

    soup=BeautifulSoup(r.text, "html.parser")
    lists=soup.findAll('tbody')
    for lst in lists:
        links=lst.findAll('a')
        for i in links:
            program_details(str(i.attrs['href']))

json_out.close()
