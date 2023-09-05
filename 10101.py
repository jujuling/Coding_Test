import sys

l=[]
for i in range(3):
    l.append(int(sys.stdin.readline()))
if l[0]==l[1]==l[2]==60:
    print("Equilateral")
elif l[0]+l[1]+l[2]!=180:
    print("Error")
elif l[0]+l[1]+l[2]==180:
    if l[0]!=l[1] and l[0]!=l[2] and l[1]!=l[2]:
        print("Scalene")
    else:
        print("Isosceles")