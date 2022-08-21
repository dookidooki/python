import this
class Car :
    def __init__(self,v_max):
        self.v_max=v_max 
    def drive(self) :
       print("이차의 최대속도 "+str(self.v_max)+"km/h로 달려요")

class Car1 :
   v_max = 0
   def drive(self) :
       print("이차의 최대속도 "+str(self.v_max)+"km/h로 달려요")       

class Car2 :
   v_max = 0
   def drive(self,v_max) :
       print("이차의 최대속도 "+str(v_max)+"km/h로 달려요")
    
c1=Car(200)
c1.drive()

c2=Car(210)
c2.drive()

c3=Car1()    
c3.v_max= 220
c3.drive()    

c4=Car1()    
c4.v_max= 230
c4.drive()

c5=Car2()
c5.drive(240)

c6=Car2()
c6.drive(250)    