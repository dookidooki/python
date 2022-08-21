# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
# key값 "1월", "2월", "3월", 1, 2, 3
 
from calendar import month


d = {}
d["1월"] = 31
d["2월"] = 28
d["3월"] = 31
print(d)

enddays = [31,28,31]
for i, ed in enumerate(enddays):
  d[i+1] = ed
print(d)

print()

md = {} 
for i in range(1,13) :
    month = str(i) + "월"
    endday = 31
    if i == 2 :
        endday = 28
    elif i in [4,6,9,11]:
        endday = 30
    md[month] = endday 
    
print(md)  
