import random, sys, os, math, gc
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from operator import mul, xor
from types import GeneratorType
# if "PyPy" in sys.version:
#     import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(2*10**5)
BUFSIZE = 8192
# MOD = 10**9 + 7
# MODD = 998244353
INF = float('inf')
D4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
D8 = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

MOD = 998244353
IMAG = 911660635
IIMAG = 86583718
rate2 = (0, 911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899, 0)
irate2 = (0, 86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235, 0)
rate3 = (0, 372528824, 337190230, 454590761, 816400692, 578227951, 180142363, 83780245, 6597683, 70046822, 623238099, 183021267, 402682409, 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204, 0)
irate3 = (0, 509520358, 929031873, 170256584, 839780419, 282974284, 395914482, 444904435, 72135471, 638914820, 66769500, 771127074, 985925487, 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681, 0)
 
def butterfly(a):
  n = len(a)
  h = (n - 1).bit_length()
  le = 0
  while le < h:
    if h - le == 1:
      p = 1 << (h - le - 1)
      rot = 1
      for s in range(1 << le):
        offset = s << (h - le)
        for i in range(p):
          l = a[i + offset]
          r = a[i + offset + p] * rot
          a[i + offset] = (l + r) % MOD
          a[i + offset + p] = (l - r) % MOD
        rot *= rate2[(~s & -~s).bit_length()]
        rot %= MOD
      le += 1
    else:
      p = 1 << (h - le - 2)
      rot = 1
      for s in range(1 << le):
        rot2 = rot * rot % MOD
        rot3 = rot2 * rot % MOD
        offset = s << (h - le)
        for i in range(p):
          a0 = a[i + offset]
          a1 = a[i + offset + p] * rot
          a2 = a[i + offset + p * 2] * rot2
          a3 = a[i + offset + p * 3] * rot3
          a1na3imag = (a1 - a3) % MOD * IMAG
          a[i + offset] = (a0 + a2 + a1 + a3) % MOD
          a[i + offset + p] = (a0 + a2 - a1 - a3) % MOD
          a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % MOD
          a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % MOD
        rot *= rate3[(~s & -~s).bit_length()]
        rot %= MOD
      le += 2
 
def butterfly_inv(a):
  n = len(a)
  h = (n - 1).bit_length()
  le = h
  while le:
    if le == 1:
      p = 1 << (h - le)
      irot = 1
      for s in range(1 << (le - 1)):
        offset = s << (h - le + 1)
        for i in range(p):
          l = a[i + offset]
          r = a[i + offset + p]
          a[i + offset] = (l + r) % MOD
          a[i + offset + p] = (l - r) * irot % MOD
        irot *= irate2[(~s & -~s).bit_length()]
        irot %= MOD
      le -= 1
    else:
      p = 1 << (h - le)
      irot = 1
      for s in range(1 << (le - 2)):
        irot2 = irot * irot % MOD
        irot3 = irot2 * irot % MOD
        offset = s << (h - le + 2)
        for i in range(p):
          a0 = a[i + offset]
          a1 = a[i + offset + p]
          a2 = a[i + offset + p * 2]
          a3 = a[i + offset + p * 3]
          a2na3iimag = (a2 - a3) * IIMAG % MOD
          a[i + offset] = (a0 + a1 + a2 + a3) % MOD
          a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % MOD
          a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % MOD
          a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % MOD
        irot *= irate3[(~s & -~s).bit_length()]
        irot %= MOD
      le -= 2
 
def multiply(s, t):
  n = len(s)
  m = len(t)
  if min(n, m) <= 60:
    a = [0] * (n + m - 1)
    for i in range(n):
      if i % 8 == 0:        
        for j in range(m):
          a[i + j] += s[i] * t[j]
          a[i + j] %= MOD
      else:
        for j in range(m):
          a[i + j] += s[i] * t[j]
    return [x % MOD for x in a]
  a = s.copy()
  b = t.copy()
  z = 1 << (n + m - 2).bit_length()
  a += [0] * (z - n)
  b += [0] * (z - m)
  butterfly(a)
  butterfly(b)
  for i in range(z):
    a[i] *= b[i]
    a[i] %= MOD
  butterfly_inv(a)
  a = a[:n + m - 1]
  iz = pow(z, MOD - 2, MOD)
  return [v * iz % MOD for v in a]

def solve():
    a = [int(i) for i in I()]
    b = [int(i) for i in I()]
    c = multiply(a, b)
    for i in range(len(c)-1, 0, -1):
        c[i-1] += c[i] // 10
        c[i] %= 10
    print("".join(map(str, c)))

    

def main():
    t = 1
    # t = II()
    for _ in range(t):
        solve()

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def bitcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c

def lcm(x, y):
    return x * y // gcd(x, y)

def lowbit(x):
    return x & -x

def perm(n, r):
    return factorial(n) // factorial(n - r) if n >= r else 0
 
def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0

def probabilityMod(x, y, mod):
    return x * pow(y, mod-2, mod) % mod

class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True
 
    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False
 
    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1
 
    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x
 
    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k
 
    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1
 
        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True
 
    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi
 
        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True
 
    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)
 
    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))
 
    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value
 
    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx
 
    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx
 
    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)
 
    def __len__(self):
        """Return the size of the sorted list."""
        return self._len
 
    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]
 
    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)
 
    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False
 
    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)
 
    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))
 
    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin = IOWrapper(sys.stdin)
# sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

def I():
    return input()

def II():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(input().split())

def LII():
    return list(map(int, input().split()))

def GMI():
    return map(lambda x: int(x) - 1, input().split())

def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))

def getGraph(n, m, directed=False):
    d = [[] for _ in range(n)]
    for _ in range(m):
        u, v = LGMI()
        d[u].append(v)
        if not directed:
            d[v].append(u)
    return d

def getWeightedGraph(n, m, directed=False):
    d = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = LII()
        u -= 1; v -= 1
        d[u].append((v, w))
        if not directed:
            d[v].append((u, w))
    return d

if __name__ == "__main__":
    main()