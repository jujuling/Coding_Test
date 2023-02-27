l=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
for i in l:
    s=s.replace(i,"*")
print(len(s))