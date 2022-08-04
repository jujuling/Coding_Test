H,M = input().split()
H=int(H)
M=int(M)

cal = 60*H+M
cal -=45

M=cal%60
H=cal//60
if H==-1:
    H+=24
print(H,M)
