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
    jobs = []

    #for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    #print(result.status_code)
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    #print(results)
    
    for result in results:
        #title = result.find("div", { "class" : "title" })
        #anchor = title.find("a")["title"] # 난 여기서 오류남..
        company = result.find("span", {"class" : "company"})
        company_anchor = company.find("a")
        if company_anchor is not None: 
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company =  company.strip() # 빈 칸 없애주기
        print(company)


    return jobs

last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)