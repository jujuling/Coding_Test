import sys

n=int(sys.stdin.readline())

dp=[-1]*1001

dp[1]=1 #SK 승
dp[2]=0 #CY 승
dp[3]=1 #SK 승

for i in range(4,n+1):
    if dp[i-1]==1 or dp[i-3]==1:
        dp[i]=0
    else:
        dp[i]=1
if dp[n]==1:
    print("SK")
else :
    print("CY")