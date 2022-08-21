end_days = [31,28,31,30,31,30,31,31,30,31,30,31]
print(len(end_days))

for i in range( 0 , len(end_days) , 1 ):
  print("""{}월은 {}일 까지""".format(i+1, end_days[i]))
  
print()  
  
for i in range (len(end_days)) :
  print("""{}월은 {}일 까지""".format(i+1, end_days[i]))