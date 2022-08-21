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