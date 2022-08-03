hour,minute ,sec=input().split()
time = int(input())
hour=int(hour)
minute=int(minute)
sec=int(sec)

sec = sec + time

while sec>59 :
    minute += (sec//60)
    sec %=60
    
while minute>59:
    hour += (minute//60)
    minute %=60
    
if hour > 23 :
    hour %=24
    
print(hour, minute, sec)
