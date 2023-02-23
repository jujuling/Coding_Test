a=[0 for i in range(30)]

for i in range(30):
    a[i]=a[i]+i+1


while True:
    try :
        n=int(input())
        a.remove(n)

    except:
        for i in range(2):
            print(a[i])
        break

