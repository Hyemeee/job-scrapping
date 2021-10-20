import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def write_file(company):
  file=open(f"{company['name']}.csv",mode="w")
  writer=csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  for job in company['jobs']:
    writer.writerow(list(job.values()))
  print(f"Completed....{company['name']}")


alba_url = "http://www.alba.co.kr" 
result=requests.get(alba_url)
soup=BeautifulSoup(result.text,"html.parser")
main= soup.find("div",{"id":"MainSuperBrand"})
superbrands=main.find_all("li",{"class":"impact"})

for brand in superbrands:
  name=brand.find("span",{"class":"company"})
  link=brand.find("a",{"class":"goodsBox-info"})
  if name and link :
    name=name.text
    link=link["href"]
    if "/" in name:
      name=name.replace("/"," ")
    
    company={"name":name,"jobs":[]}

    result2=requests.get(link)
    soup2=BeautifulSoup(result2.text,"html.parser")
    tbody=soup2.find("div",{"id":"NormalInfo"})
    rows=tbody.find_all("tr",{"class":""})

    for row in rows:

      local=row.find("td",{"class":"local first"})
      if local:
        local=local.text

      title=row.find("td",{"class":"title"})
      if title:
        title=title.find("a").find("span",{"class":"company"}).text
      
      time =row.find("td",{"class":"data"})
      if time:
        time=time.text
      
      pay=row.find("td",{"class":"pay"})
      if pay:
        pay=pay.text
      
      date=row.find("td",{"class":"regDate late"})
      if date:
        date=date.text
      
      job={'place':local,'title':title,'time':time,'pay':pay,'date':date}

      company['jobs'].append(job)
  
#write_file(company)







