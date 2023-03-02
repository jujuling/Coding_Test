from sys import stdin

n,m=(map(int, stdin.readline().split()))
a=[]
b=[]
for _ in range(n):
    a.append(stdin.readline().rstrip())
for _ in range(m):
    b.append(stdin.readline().rstrip())

c=set(a)&set(b)
print(len(c))
for i in sorted(c):
    print(i)