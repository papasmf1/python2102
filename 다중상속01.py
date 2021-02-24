#이름이 충돌(다중 상속)
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self):
        print("호랑이 어흥~~")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으르릉~~")

class Liger(Lion, Tiger):
    def play(self):
        print("라이거와 놀기")


l = Liger()
l.cry() 
print( "MRO:{0}".format(Liger.__mro__) )

        
