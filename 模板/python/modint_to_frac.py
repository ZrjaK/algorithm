def modint_to_frac(a,mod):
  a%=mod
  if a==0:
    return '0/1'
  for X in range(1,10000):
    Y=a*X%mod
    if 0<Y<10000:
      return str(Y)+'/'+str(X)
    if mod-10000<Y<mod:
      return '-'+str(mod-Y)+'/'+str(X)
  return 'inexpressible'