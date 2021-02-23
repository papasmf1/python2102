#전역변수와 지역변수 이름 충돌 
x = 1 
def func(a):
    return x+a 

#호출
print(func(1) )

def func2(a):
    x = 5 
    return x+a 

#호출
print(func2(1) )

#불변형식
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))

#가변형식
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#가변형식(입출력이 자유롭다~~)
def change(x):
    #이번에는 복사본을 사용
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:{0}".format(x1))

#호출
wordlist = ["J","A","M"]
change(wordlist)
print(wordlist)

#외부에 있는 전역변수를 읽기/쓰기하는 경우(불변형식)
g = 1 
def testScope(a):
    #global g 
    g = 2 
    return a + g 

#호출
print( testScope(1) )
print("g:{0}".format(g) )


#기본값(default value)
def times(a=10, b=20):
    return a*b 

print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자 방식
def connectURI(server, port):
    str = "http://" + server + ":" + port
    return str 

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port="8080", server="test.com"))


