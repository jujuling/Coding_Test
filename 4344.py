c=int(input())

for _ in range(c):
    s=list(map(int,input().split()))
    num=0
    avg=sum(s[1:])/s[0] #첫 번째가 학생수, idx 1~끝까지가 점수

    for i in range(1,len(s)):
        if s[i]>avg:
            num=num+1
    print("%.3f%%" %(num/s[0]*100))