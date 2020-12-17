# #2. Building & Job scrapper

### #2.0 What is web scrapping

Web scrapping 이란?

- 웹 상의 데이터를 추출하는 것
- 예제 : 신문 기사 긁어올 때 이미지랑 헤드라인 간단하게 보여주는 것.
- 구글 검색 시, 정보 간단하게 보여주는 것.

### #2.1 What are we building

- indeed , stack overflow 사이트에서 정보 가져오기
- 페이지 자동으로 넘어가고 정보 얻고 엑셀에 저장하는 것 모두 자동화

### #2.2 Navigating with Python

- indeed로 접근하기
- 몇 페이지인지 알아내기

### #2.3 Extracting Indeed pages

- requests와 beautifulsoup4 설치 완료.
- vscode 에서 문제가 있었는데 interpreter 설정 제대로 해주니 해결됨.

```python
print(indeed_result.text) # response 200 : okay , getting html
```

- requests.get(url.text) : html 전부 긁어오기
- span