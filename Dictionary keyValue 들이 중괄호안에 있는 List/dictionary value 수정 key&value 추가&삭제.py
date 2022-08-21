from curses import keyname


m = {"1월":31, "2월":28, "3월":31}

m["4월"]=30   #추가하기

print(m)

del m["1월"]    #삭제하기

print(m)

