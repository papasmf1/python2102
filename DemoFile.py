# DemoFile.py 
# 파일을 생성
f = open("c:\\work\\test.txt", "wt")
f.write("abcd\n한글\n1234\n")
f.close()

#파일을 읽기 
f = open("c:\\work\\test.txt", "rt")
#파일 전체를 읽어서 문자열 변수로 리턴 
print( f.read() )

#어디쯤 읽기있어? 
print( f.tell() )
#맨 첫줄 처음으로 리셋 
f.seek(0)
print( f.readline() )
print( f.readline() )

#이번에는 리스트로 리턴 
print("===readlines()===")
f.seek(0)
result = f.readlines()
for item in result:
    print(item.replace("\n", ""))

f.close() 
