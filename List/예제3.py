print("== 예제 3 ==")
s = "a안b녕c하d세e요f"

print("s를 이루는 문자 중에서 한글만 출력")
# 구현
print(s[1]+s[3]+s[5]+s[7]+s[9])

print("s를 이루는 문자 중에서 한글만 출력, for, if, or, continue")
# 구현
for c in s:
    if c=='a' or c=='b' or c=='c' or c=='d' or c=='e' or c=='f':
        continue
    print(c, end='')
print()

print("s를 이루는 문자 중에서 한글만 출력, for, if, and, 방법 2")
# 구현
for c in s:
    if c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f':
        print(c, end='')
print()

print("s를 이루는 문자 중에서 한글만 출력, for, not in, 방법 3")
# 구현
for c in s  :
    if c not in ['a','b','c','d','e','f']:
        print(c,end='')
    else:
        print('',end='')
