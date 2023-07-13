import sys

x,y=map(int,sys.stdin.readline().split())

days=[31,28,31,30,31,30,31,31,30,31,30,31]
yoil=['SUN','MON','TUE','WED','THU','FRI','SAT']

hap=0
for i in range(x-1):
    hap+=days[i]
hap+=y
print(yoil[hap%7])