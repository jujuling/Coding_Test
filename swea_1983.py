#import sys
#sys.stdin=open('input.txt','r')

T=int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1,T+1):
    n,k=map(int,input().split())
    hak=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        total=a*0.35+b*0.45+c*0.2
        hak.append(total)
    k_score=hak[k-1]
    hak.sort(reverse=True)
    result=hak.index(k_score)
    result//=(n//10)
    print("#%d %s" %(t,score[result]))

