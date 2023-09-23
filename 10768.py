import sys

mon=int(sys.stdin.readline())
day=int(sys.stdin.readline())

if mon>2:
    print("After")
elif mon<2:
    print("Before")
else: #mon==2
    if day<18:
        print("Before")
    elif day>18:
        print("After")
    else:
        print("Special")