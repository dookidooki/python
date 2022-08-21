print("== 예제 2 ==")
s = "안녕하세요"

print("s를 이루는 문자를 하나씩 출력, while")
# 구현
i=0
while i<len(s):
    print(s[i], end=' ')
    i+=1

print()

print("s를 이루는 문자를 역순으로 하나씩 출력, while")
# 구현
i=len(s)-1
while i>-1:
    print(s[i], end=' ')
    i-=1

print()
print("s를 이루는 문자를 하나씩 출력, for")
# 구현
for i in range(len(s)):
    print(s[i], end=' ')