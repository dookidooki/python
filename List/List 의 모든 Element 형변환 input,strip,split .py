
print('''list에 를 입력받아서 만든다음에
좌우 공백을 없앱니다
이때 공백 수 만큼 Element가 생성됩니다
list의 값을 a,b,c에 int로 넣을 겁니다
ex) 1 2 3 ''')
l1= input().strip().split(' ')
print(l1)

a,b,c = map(int, l1)
print(a,b,c)

l1 =list(map(int, l1))
print(l1)

print(l1[0]+l1[1]+l1[2])  