import sys
s=sys.stdin.readline().rstrip()

for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        tmp=ord(s[i])+13
        if tmp>ord('z'):
            tmp=chr(tmp-26)
        else:
            tmp=chr(tmp)
        print(tmp,end='')
    elif s[i]>='A' and s[i]<='Z':
        tmp=ord(s[i])+13
        if tmp>ord('Z'):
            tmp=chr(tmp-26)
        else:
            tmp=chr(tmp)
        print(tmp,end='')
    else:
        print(s[i],end='')