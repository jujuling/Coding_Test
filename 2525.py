hour,minute =input().split()
time = int(input())
hour=int(hour)
minute=int(minute)

cal = minute + time
while(1) :
    
    if cal>59 :
        hour +=1
        cal -=60
        
    else :
        break
if hour > 23 :
    hour -=24
    
print(hour, cal)
