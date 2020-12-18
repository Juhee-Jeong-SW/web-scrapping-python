import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&fromage=any&limit={}".format(LIMIT)

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    #print(indeed_result.text) # response 200 : okay , getting html

    soup = BeautifulSoup(result.text, "html.parser")

    #print(indeed_soup)
    pagination = soup.find("div", {"class" : "pagination"})

    #print(pagination)

    pages = pagination.find_all('a')
    spans = []
    #print(pages)

    for page in pages[:-1]:
        spans.append(int(page.find("span").string))

    max_page = spans[-1]

    return max_page

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        print(result.status_code)

last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)