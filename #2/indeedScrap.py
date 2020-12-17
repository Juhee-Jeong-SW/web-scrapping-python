import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&fromage=any&limit=50")

#print(indeed_result.text) # response 200 : okay , getting html

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

#print(indeed_soup)
pagination = indeed_soup.find("div", {"class" : "pagination"})

#print(pagination)

pages = pagination.find_all('a')
spans = []
#print(pages)

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])


