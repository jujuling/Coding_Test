import sys

while True:
    result=0
    s=sys.stdin.readline().strip()
    s=s.lower()
    if s[0]=="#" and len(s)==1:
        break
    result += s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
    print(result)