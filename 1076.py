import sys

j=['black','brown','red','orange','yellow','green','blue','violet','grey','white']


n1=sys.stdin.readline().strip()
n2=sys.stdin.readline().strip()
n3=sys.stdin.readline().strip()

print((j.index(n1)*10 + j.index(n2)) * 10**j.index(n3))