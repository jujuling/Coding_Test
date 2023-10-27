import sys

n=int(sys.stdin.readline())

l=[]
for i in range(n):
    name,day,month,year=map(str,sys.stdin.readline().strip().split())
    l.append([name,int(day),int(month),int(year)])

#나이가 많은 사람 순으로 정렬됨
l.sort(key=lambda x: (x[3],x[2],x[1]))

print(l[-1][0]) #가장 나이가 적은 사람은 마지막임(-1)
print(l[0][0])