# class class이름 :
#     데이터구조
#     데이터구조를 이용한 함수(self)


class Person :
    name = ""
    age = 0
    address =""
    def introduce(self,name,age,address):
        print(name)
        print(age)
        print(address)
        
p1 = Person()
p1.name = "홍길동"
p1.age = 25
p1.address ="대전"

p1.introduce("홍길동",25,"대전")
# Person.introduce(p1)


p2 = Person()