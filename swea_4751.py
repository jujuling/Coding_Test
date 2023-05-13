#import sys
#sys.stdin = open("input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    s=list(input())
    l=len(s)
    n1='..#.'
    n2='.#'
    n3='#.'
    print(n1*l+'.')
    print(n2*l*2+'.')
    for i in range(l):
        print(n3+s[i]+'.',end='')
    print('#')
    print(n2*l*2+'.')
    print(n1*l+'.')

