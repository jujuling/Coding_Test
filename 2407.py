import sys
import math
n,m=map(int,sys.stdin.readline().split())

nf=math.factorial(n)
mf=math.factorial(m)
n_mf=math.factorial(n-m)

print(nf//(mf*n_mf))