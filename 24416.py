import sys

def fib(n):
    a,b=1,1
    for i in range(n-2):
        a,b=b,a+b
    return b

def fibonacci(n):
    return n-2

n=int(sys.stdin.readline())

print(fib(n),fibonacci(n))