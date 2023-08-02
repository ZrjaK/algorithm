from sys import stdin
input=lambda :stdin.readline()[:-1]

h,w,q=map(int,input().split())
S=[[int(x) for x in input().split()] for i in range(h)]

def calc(n,rot):
  now=0
  for i in range(0,len(rot)//2):
    x=rot[2*i]
    y=rot[2*i+1]
    if y<=x:
      now+=x-y
    else:
      now+=n-(y-x)
    #print(now)
    now%=n
  res=[0]*n
  for i in range(n):
    res[i]=(now+i)%n
  if len(rot)%2==1:
    x=rot[-1]
    res1=res[:x+1]
    res2=res[x+1:]
    res=res1[::-1]+res2[::-1]
  #print(res)
  return res

rot1=[]
rot2=[]
f = 0
for _ in range(q):
  T=list(map(lambda x:int(x),input().split()))
  if T[0] == 1:
    a, b = T[1:]
    a -= 1
    b -= 1
    if f:
      a, b = b, a
    rot1.append(a)
    rot2.append(b)
  if T[0] == 2:
    f ^= 1

res1=calc(h,rot1)
res2=calc(w,rot2)

if not f:
    ans=[[0]*w for i in range(h)]
else:
  ans=[[0]*h for i in range(w)]
for i in range(h):
  for j in range(w):
    if not f:
        ans[i][j]=S[res1[i]][res2[j]]
    else:
        ans[j][i] = S[res1[i]][res2[j]]

for i in ans:
  print(*i)