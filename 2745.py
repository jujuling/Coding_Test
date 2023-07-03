import sys

n,b=map(str,sys.stdin.readline().split())
b=int(b)
flag="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
st=[]

for i in range(len(n)):
    idx=flag.index(n[i])
    st.append(idx)

result=0
for i in range(len(st)):
    result+=st[len(st)-1-i]*(b**i)
print(result)