a = "   <-왼쪽 공백 제거   "
print(a)
print(a.lstrip())

b = "   오른쪽 공백제거->   "
print(b, end = "-")
print(b.rstrip(),end = "-")

print() 

print("" "" "" "사과,포도,복숭아" "" "" " 입력하세요")
a = input()
print(a)
a = a.strip()
print(a)
a= a.split(',') #,을 기준으로 나누기
print(a)   

print("" "" "" "사과,포도,복숭아" "" "" " 입력하세요")
a =input().strip().split(',')
print(a)


