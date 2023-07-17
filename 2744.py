import sys

s=list(sys.stdin.readline().strip())

for i in s:
    #print(i)
    if i>='A' and i<='Z':
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')