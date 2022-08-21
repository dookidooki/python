
# items 는 key:value 요소를 두개로 나누어주어야 한다
# 이것을 튜플을 압축풀기 라고 한다

# key와 value 하나 제거하고싶다
# del dict Name[ key ] 

# 딕셔너리이름.
# keys()
# values()
# items()
# clear()

md = { "1월" : 31, "2월": 28, "3월":31 }


for i in md.keys() :
    print(i+"은 "+str(md[i])+"일 까지")
   
   
for i in md.values() : 
    print(str(i)+"일 까지")
    
for i,j in md.items() : 
    print(i+"은",str(j)+"일 까지")
    
print(md)

del md["3월"]
print(md)

md.clear()
print(md)
