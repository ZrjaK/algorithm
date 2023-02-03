x=[]
y=[]
z=[1,2,3,4,5,6,7,8,9]
t=0
h=dict(zip((6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24),(10000,36,720,360,80,252,108,72,54,180,72,180,119,36,306,1080,144,1800,3600)))
for i in range(3):
    a=[int(i) for i in input().split()]
    x.append(a)
for i in x:
    for j in i:
        y.append(j)
        t+=1
f=0
for i in z:
    if i not in y:
        f=i
for i in range(3):
    for j in range(3):
        if x[i][j]==0:
            x[i][j]=f
for i in range(3):
    n,m=map(int,input().split())
    print(x[n-1][m-1])
g=int(input())
if g>=1 and g<=3:
    print(h[sum(x[g-1])])
if g>=4 and g<=6:
    print(h[x[0][g-4]+x[1][g-4]+x[2][g-4]])
if g==7:
    print(h[x[0][0] + x[1][1] + x[2][2]])
if g==8:
    print(h[x[2][0] + x[1][1] + x[0][2]])
