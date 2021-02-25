# web1.py 
from bs4 import BeautifulSoup

#문서를 로딩
page = open("c:\\work\\test01.html","rt", encoding="utf-8").read() 
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#<p>를 모두 가져오기 
#리턴형이 List
#print( soup.find_all("p") )

#첫번째 <p>태그 검색 
#print( soup.find("p") )

#조건이 있는 경우(필터링) <p class="outer-text">컨텐츠</p>
#print( soup.find_all("p", class_="outer-text") )

#반복구문으로 가져오기
#<p>내용물</p>
for tag in soup.find_all("p"):
    #태그를 삭제하고 알맹이에서 공백문자를 제거 
    print(tag.text.strip() ) 
