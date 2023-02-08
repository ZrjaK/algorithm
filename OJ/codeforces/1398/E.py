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
MOD = 10**9 + 7
MODD = 998244353
INF = float('inf')
D4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
D8 = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)
 
    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot , nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1,nd_.cnt)
 
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])
 
    def append(self, v):
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
 
                return 0
            else:
                nd.cnt+=1
                nd.sum+=v-1
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break
 
    def kth(self,k):
        cnt=k
        nd=self.root
        while True:
            if nd.left:
                if nd.left.cnt<k:
                    k-=nd.left.cnt+1
                    if nd.right:
                        nd=nd.right
                    else:
                        raise IndexError("BalancingTree doesn't hold kth number")
                elif nd.left.cnt==k:
                    return nd.value-1
                else:
                    nd=nd.left
            else:
                if k==0:
                    return nd.value-1
                if nd.right:
                    k-=1
                    nd=nd.right
                else:
                    raise IndexError("BalancingTree doesn't hold kth number")
 
    def kth_sum(self,k):
        if k==-1:
            return 0
        cnt=k
        res_sum=0
        nd=self.root
        while True:
            if nd.left:
                if nd.left.cnt<k:
                    k-=nd.left.cnt+1
                    res_sum+=nd.left.sum+nd.value-1
                    if nd.right:
                        nd=nd.right
                    else:
                        raise IndexError("BalancingTree doesn't hold kth number")
                elif nd.left.cnt==k:
                    res_sum+=nd.left.sum+nd.value-1
                    return res_sum
                else:
                    nd=nd.left
            else:
                if k==0:
                    return res_sum+nd.value-1
                if nd.right:
                    k-=1
                    res_sum+=nd.value-1
                    nd=nd.right
                else:
                    print(cnt,self.size,nd.value-1,nd.right)
                    self.debug()
                    raise IndexError("BalancingTree doesn't hold kth number")
 
    def kth_sum_big(self,k):
        res_sum=self.sum
        if self.size>k:
            res_sum-=self.kth_sum(self.size-k-2)
            return res_sum
        else:
            raise IndexError("BalancingTree doesn't hold kth number")
 
    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd
 
    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd
 
    def find_l(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1
 
    def find_r(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1
 
    @property
    def max(self):
        if self.size:
            return self.find_l((1<<self.N)-1)
        return 0
 
    @property
    def min(self):
        if self.size:
            return self.find_r(-1)
        return 0
 
    @property
    def sum(self):
        return self.root.sum-self.root.value+1
 
    @property
    def size(self):
        return self.root.cnt-1
 
    def delete(self, v, nd = None, prev = None):
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            nd.cnt-=1
            nd.sum-=v-1
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        nd.cnt-=1
        nd.sum-=v-1
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right=None
            elif not prev.right:
                prev.left=None
            else:
                if nd.pivot==prev.left.pivot:
                    prev.left=None
                else:
                    prev.right=None
        elif nd.right:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)
        else:
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)
 
 
    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v
 
    def __len__(self):
        return self.size
 
    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None
            self.cnt=1
            self.sum=v-1

def solve():
    n = II()
    s = 0
    double = BalancingTree(30)
    tree = [BalancingTree(30) for _ in range(2)]
    ans = []
    for _ in range(n):
        t, d = LII()
        if d > 0:
            tree[t].append(d)
            double.append(d)
        else:
            tree[t].delete(-d)
            double.delete(-d)
        s += d
        m = len(tree[1])
        x, y = double.kth_sum_big(m - 1), tree[1].sum
        if m and x == y:
            ans.append(s + x - tree[1].min + tree[0].max)
        else:
            ans.append(s + x)
    print(*ans, sep='\n')

    

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