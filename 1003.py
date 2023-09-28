import sys

def fib(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if len(zero)<=n:
        for i in range(len(zero),n+1):
            zero.append(one[-1])
            one.append(one[-1]+zero[-2])
    print(zero[n],one[n])

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    fib(n)