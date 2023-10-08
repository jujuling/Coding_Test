import sys

s=sys.stdin.readline()
result=0
mo=['a','e','i','o','u']
for i in s:
    if i in mo:
        result+=1
print(result)