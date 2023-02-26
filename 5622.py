s=input()

l=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]


total=0
for i in range(len(s)):
    for j in range(8):
        tmp=l[j]
        for k in range(len(tmp)):
            if s[i]==tmp[k]:
                total =total +j+2
                break
print(total+len(s))