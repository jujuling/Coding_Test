import sys

n=int(sys.stdin.readline())
enter=set()

for i in range(n):
    l=list(map(str,sys.stdin.readline().strip().split()))
    if l[1]=='enter':
        enter.add(l[0])
    else:
        if l[0] in enter :
            enter.remove(l[0])

enter=list(enter)
enter.sort(reverse=True)
for i in enter:
    print(i)