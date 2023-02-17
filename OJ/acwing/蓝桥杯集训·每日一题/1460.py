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

from collections import defaultdict


def sa_naive(s):
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda x: s[x:])
    return sa


def sa_doubling(s):
    n = len(s)
    sa = list(range(n))
    rnk = s
    tmp = [0] * n
    k = 1
    while k < n:
        sa.sort(key=lambda x: (rnk[x], rnk[x + k])
        if x + k < n else (rnk[x], -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]]
            if sa[i - 1] + k < n:
                x = (rnk[sa[i - 1]], rnk[sa[i - 1] + k])
            else:
                x = (rnk[sa[i - 1]], -1)
            if sa[i] + k < n:
                y = (rnk[sa[i]], rnk[sa[i] + k])
            else:
                y = (rnk[sa[i]], -1)
            if x < y:
                tmp[sa[i]] += 1
        k *= 2
        tmp, rnk = rnk, tmp
    return sa


def sa_is(s, upper):
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]
    if n < 10:
        return sa_naive(s)
    if n < 50:
        return sa_doubling(s)
    ls = [0] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if s[i] == s[i + 1] else s[i] < s[i + 1]
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if ls[i]:
            sum_l[s[i] + 1] += 1
        else:
            sum_s[s[i]] += 1
    for i in range(upper):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]
    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)
    sa = [-1] * n
    buf = sum_s.copy()
    for d in lms:
        if d == n:
            continue
        sa[buf[s[d]]] = d
        buf[s[d]] += 1
    buf = sum_l.copy()
    sa[buf[s[n - 1]]] = n - 1
    buf[s[n - 1]] += 1
    for i in range(n):
        v = sa[i]
        if v >= 1 and not ls[v - 1]:
            sa[buf[s[v - 1]]] = v - 1
            buf[s[v - 1]] += 1
    buf = sum_l.copy()
    for i in range(n - 1, -1, -1):
        v = sa[i]
        if v >= 1 and ls[v - 1]:
            buf[s[v - 1] + 1] -= 1
            sa[buf[s[v - 1] + 1]] = v - 1
    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l = sorted_lms[i - 1]
            r = sorted_lms[i]
            end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
            end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r += 1
                if l == n or s[l] != s[r]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s, rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        sa = [-1] * n
        buf = sum_s.copy()
        for d in sorted_lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l.copy()
        sa[buf[s[n - 1]]] = n - 1
        buf[s[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[s[v - 1]]] = v - 1
                buf[s[v - 1]] += 1
        buf = sum_l.copy()
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[s[v - 1] + 1] -= 1
                sa[buf[s[v - 1] + 1]] = v - 1
    return sa


def suffix_array(s, upper=255):
    if type(s) is str:
        s = [ord(c) for c in s]
    return sa_is(s, upper)

class SuffixArray:

    def __init__(self, s):
        self.sa = suffix_array(s)
        self.rk = self._rk(self.sa)
        self.height = self._height(s)

    def _count_sort(self, ls):
        c = defaultdict(list)
        for i, v in enumerate(ls):
            c[v].append(i)
        ans = []
        for v in sorted(list(c.keys())):
            for k in c[v]:
                ans.append((k, v))
        return ans

    def _rk(self, sa):
        rk = [0 for _ in sa]
        for i in range(len(sa)):
            rk[sa[i]] = i
        return rk

    def _height(self, s):
        sa, rk = self.sa, self.rk
        ht = [0] * len(sa)
        k = 0
        for sai in range(0, len(s)):
            if k:
                k -= 1
            while True:
                ai, bi = sai + k, sa[rk[sai] - 1] + k
                if not (0 <= ai < len(s) and 0 <= bi < len(s)):
                    break
                if max(ai, bi) >= len(s):
                    break
                elif s[ai] == s[bi]:
                    k += 1
                else:
                    break
            ht[rk[sai]] = k
        return ht

# https://oi-wiki.org/string/sa/

# sa 数组：字典序排名为 i 的后缀是第几个；
# rk 数组：第 i 个后缀的排名是多少（不难发现 rk 与 sa 满足 sa[rk[i]] = rk[sa[i]] = i）；
# height 数组：存储 sa[i] 与 sa[i - 1] 的 LCP（最长公共前缀） 为何值。

def solve():
    n = II()
    s = I()
    sa = SuffixArray(s)
    print(max(sa.height) + 1)
    

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