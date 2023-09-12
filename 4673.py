l=[]
def self_n(n):
    dn=n
    n=str(n)
    for i in n:
        dn+=int(i)
    l.append(dn)

for i in range(1,10001):
    self_n(i)

for i in range(1,10001):
    if i not in l:
        print(i)