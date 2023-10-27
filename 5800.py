import sys

k=int(sys.stdin.readline())
for i in range(k):
    l=list(map(int,sys.stdin.readline().split()))
    l.remove(l[0])
    l.sort(reverse=True)
    print("Class %d" %(i+1))
    gap=[]
    for j in range(len(l)-1):
        gap.append(l[j]-l[j+1])
    print("Max %d, Min %d, Largest gap %d" %(max(l),min(l),max(gap)))