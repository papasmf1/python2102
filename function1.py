# function1.py 
#함수 정의
def setValue(newValue):
    x = newValue
    print(x)

#함수 호출
result = setValue(5)
print(result)

#값을 리턴하는 함수
def swap(x,y):
    return y,x 

#호출
result = swap(5,6)
print(result)
print(result[0], result[1])

#문자의 교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #내부에 지역변수에 값을 모아두기 
    #이름 규칙(카멜 표기법)
    retList = [] 
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출(중단점, Break Point)
result = intersect("HAM","SPAM")
print(result)
