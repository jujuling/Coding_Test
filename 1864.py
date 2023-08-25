import sys

dic = {'-':0, '\\':1, '(':2,'@':3,'?':4, '>':5, '&':6, '%':7, '/':-1}
while True:
  l=list(sys.stdin.readline().strip())
  if len(l)==1 and l[0]=='#':
    break
  lnum=[]
  for i in range(len(l)):
    if l[i] in dic :
      lnum.append(dic[l[i]])
  result=0
  lnum.reverse()
  flag=0
  for i in range(len(l)):
    result+=((8**flag)*lnum[i])
    flag+=1
  print(result)