# 문제 : for문으로 구구단 8단 출력
print("for문으로 구구단 8단 출력")
for i in range(1, 10):
    print('8 * {} = {}'.format(i, 8 * i))

print()

print("for문으로 구구단 출력")
for dan in range(2, 10):
    print('==={}단==='.format(dan))
    for i in range(1, 10):
        print('{} * {} = {}'.format(dan, i, dan * i))