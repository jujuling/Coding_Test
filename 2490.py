import sys

for i in range(3):
    l=list(map(int,sys.stdin.readline().split()))
    if l.count(1)==0:
        print("D")
    elif l.count(1)==4:
        print("E")
    elif l.count(1)==3:
        print("A")
    elif l.count(1)==2:
        print("B")
    else:
        print("C")