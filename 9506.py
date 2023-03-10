while True:
    n=int(input())
    if n ==-1:
        break
    l=list()
    for i in range(1,n//2+1):
        if n%i==0:
            l.append(i)
    if n==sum(l):
        print("%d = " %n, end="")
        for j in range(len(l)-1):
            print("%d + " %l[j], end="")
        print("%d" %l[-1])
    else:
        print("%d is NOT perfect." %n)