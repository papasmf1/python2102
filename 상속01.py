#부모 클래스 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 
class Student(Person):
    #메서드 덮어쓰기(재정의)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #다중 라인 주석 처리: ctrl + / 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo() 


