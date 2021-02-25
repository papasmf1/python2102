# DemoRE.py 
#정규 표현식
import re 

# #match함수는 정확하게 일치(숫자만 경우의 수가 0~N th) 
# print( re.match("[0-9]*th", "35th") )
# #search함수는 포함하고 있으면 검색 
# print( re.search("[0-9]*th", "35th") )

#약간의 함수(match, search함수 차이)
# print( bool(re.match("[0-9]*th", "  35th")) )
# print( bool(re.search("[0-9]*th", "  35th")) )

#특정 문자열 패턴 
# 다중 라인 주석 처리: ctrl + / 
# print( bool(re.match("ap", "this is apple")) )
# print( bool(re.search("ap", "this is apple")) )

#우편번호 패턴
# print( bool(re.match("\d{5}", "우리동네는 51200")) )
# print( bool(re.search("\d{5}", "우리동네는 51200")) )

#전화번호 패턴
telChecker = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")
print( bool(telChecker.match("02-3429-5000")) )
print( bool(telChecker.match("02-3429가-5000")) )
print( bool(telChecker.match("1234-3429-5000")) )

#결과를 받아서 처리(매칭 오브젝트)
m = telChecker.match("02-3429-5000")
print( m.group() )
print( m.group(1) )
print( m.group(2) )
print( m.groups() )

