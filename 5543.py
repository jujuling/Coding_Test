import sys

sang=int(sys.stdin.readline())
joong=int(sys.stdin.readline())
ha=int(sys.stdin.readline())
cola=int(sys.stdin.readline())
cider=int(sys.stdin.readline())

result=min(sang,joong,ha)+min(cola,cider)-50

print(result)