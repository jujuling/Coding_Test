import sys

s=sys.stdin.readline().strip()
l=[]

for i in range(len(s)):
    l.append(s[i:len(s)])

l.sort()
for i in l:
    print(i)