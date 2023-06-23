import sys
s=sys.stdin.readline().strip()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt=[0]*26

for i in range(len(s)):
    if s[i] in l:
        cnt[l.index(s[i])]+=1

for i in cnt:
    print(i,end=' ')