#연산자 오버라이드(파이썬은 연산자 재정의) 
# object클래스에 정의된 메서드(+,-,*,/)
# 문자열:   "ac" + "cd"  이항 연산자 ==> "abcd"
# 정수: 100 + 20  ==> 120 
class NumBox:
	#생성자
	def __init__(self, num):
		self.Num = num
	#일반 메서드 
	def add(self, num):
		self.Num += num
	#일반 메서드 
	def remove(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100)
print(n.Num)
n.remove(30)
print(n.Num)
