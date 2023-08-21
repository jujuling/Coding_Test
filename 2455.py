import sys

maxp=0
train=0
for i in range(4):
    outp, inp=map(int,sys.stdin.readline().split())
    train-=outp
    train+=inp
    if train>maxp :
        maxp=train
print(maxp)