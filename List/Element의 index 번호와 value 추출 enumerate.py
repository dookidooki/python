#enumerate

#for 순서매길 매개변수 (i), 0번인덱스의 value값(letter) 
#in enenumerate (List, start=x) :
#print(i,letter)

# i =x+0, x+1, +2, x+3...
# letter = [0], [1], [2], [3]...


end_days = [31,28,31,30,31,30,31,31,30,31,30,31]

for m,d in enumerate (end_days, start=1) :
  print("""{}월은 {}일 까지""".format(m,d))

print()

for i,letter in enumerate (['사과','바나나','딸기','메론',
                            '토마토', '수박'], start=2) :
    print(i)
    print(letter)
    print(i,letter)
    print()
    # 출력되는 index 번호 = index 번호 + start
    
