s=input()
total=10

for i in range(len(s)):
    if i==0:
       continue
    if s[i-1]==s[i]:
        total +=5
    else:
        total +=10
print(total)