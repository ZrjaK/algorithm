n, A, B, k1, k2 = map(int, input().split())
s = list(input())

class segtree():
  def __init__(self,init,func,ide):
    self.n=len(init)
    self.func=func
    self.ide=ide
    self.size=1<<(self.n-1).bit_length()
    self.tree=[self.ide for i in range(2*self.size)]
    for i in range(self.n):
      self.tree[self.size+i]=init[i]
    for i in range(self.size-1,0,-1):
      self.tree[i]=self.func(self.tree[2*i], self.tree[2*i|1])
  
  def update(self,k,x):
    k+=self.size
    self.tree[k]=x
    k>>=1
    while k:
      self.tree[k]=self.func(self.tree[2*k],self.tree[k*2|1])
      k>>=1
  
  def get(self,i):
    return self.tree[i+self.size]
  
  def query(self,l,r):
    l+=self.size
    r+=self.size
    l_res=self.ide
    r_res=self.ide
    while l<r:
      if l&1:
        l_res=self.func(l_res,self.tree[l])
        l+=1
      if r&1:
        r-=1
        r_res=self.func(self.tree[r],r_res)
      l>>=1
      r>>=1
    return self.func(l_res,r_res)
 
  def __iter__(self):
    for i in range(self.n):
      yield self.tree[i+self.size]
          
  def __str__(self):
    return str(list(self))

def fun(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][k] += a[i][j] * b[j][k]
                res[i][k] %= int(1e9 + 7)
    return res

def idle():
    res = [[1, 0], [0, 1]]
    return res

seg = segtree([idle() for _ in range(n)], fun, idle())

for i in range(n):
    if s[i] == "0":
        seg.update(i, [[k1, 0], [1, 1]])
    else:
        seg.update(i, [[1, 1], [0, k2]])
        

q = int(input())
for _ in range(q):
    x = int(input()) - 1
    if s[x] == "1":
        s[x] = "0"
        seg.update(x, [[k1, 0], [1, 1]])
    else:
        s[x] = "1"
        seg.update(x, [[1, 1], [0, k2]])
    res = seg.tree[1]
    a = A * res[0][0] + B * res[1][0]
    a %= int(1e9 + 7)
    b = A * res[0][1] + B * res[1][1]
    b %= int(1e9 + 7)
    print(a, b)