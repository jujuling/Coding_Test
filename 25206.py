sc=['A+','A0','B+','B0','C+','C0','D+','D0','F','P']
sc_n=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
hak=0

total =0
for i in range(20):
    a,b,c= map(str,input().split())
    if c==sc[9]:
        continue
    hak=hak+float(b)
    idx=sc.index(c)
    total = total + float(b)* (sc_n[idx])

print("%f" %(total/hak))