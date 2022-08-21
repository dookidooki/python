# 문제 : 자동차가 3번 달리게 해주세요.
# 출력 : 자동차가 달립니다.

# v1. 1개의 자동차가 3번 달리게 해주세요.

# v2. 3개의 자동차가 1번씩 달리게 해주세요.

# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.
# 자동차가 달립니다.

class Car :
    number = 0
    def run(self) :
        print("자동차가 달립니다")
        
c1 = Car()    #객체 생성     
c1.number=1   #객체에게 value 주기

c1.run()
c1.run()
c1.run()

c2 = Car()
c2.number=2
c3 = Car()       
c2.number=3

c1.run()
c2.run()
c3.run()