# web2.py 
#웹서버와 통신
#수정 
import urllib.request
#뷰티플스프 
from bs4 import BeautifulSoup 


#네이버에 페이지 실행을 요청 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri") 

#검색이 용이한 객체 생성
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
#   <a href="/webtoon/detail.nhn">마음의 소리 49화 &lt;지혜&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)) )

#첫번째 방을 슬라이싱 
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#반복문
for tag in cartoons:
    title = tag.find("a").text 
    print(title.strip() )
    
