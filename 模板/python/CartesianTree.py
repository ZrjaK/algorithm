def CartesianTree(a):
  N=len(a)
  p=[-1]*N
  stc=[]
  g=[[] for i in range(N)]
  for i in range(N):
    prv=-1
    while len(stc) and a[i]<a[stc[-1]]:
      prv=stc.pop()
    if prv!=-1:
      p[prv]=i
    if stc:
      p[i]=stc[-1]
    stc.append(i)
  
  root=-1
  for i in range(N):
    if p[i]!=-1:
      g[p[i]].append(i)
    else:
      root=i
  
  return g,root