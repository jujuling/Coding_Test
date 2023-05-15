#import sys
#sys.stdin=open('sample_input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    nlist=list(map(str,input().split()))
    a=[]
    b=[]
    cut=int(n/2+0.5)
    for i in range(cut):
        a.append(nlist[i])
    for i in range(cut,n):
        b.append(nlist[i])

    print("#%d" %test_case, end=' ')
    if n%2==0:
        for i in range(cut):
            print(a[i],end=' ')
            print(b[i],end=' ')
    else:
        print(a[0], end=' ')
        for i in range(cut-1):
            print(b[i],end=' ')
            print(a[i+1],end=' ')
    print()