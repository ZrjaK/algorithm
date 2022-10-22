import sys, os, math, random, threading
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
from bisect import bisect_left, bisect_right, insort, insort_left, insort_right
# sys.setrecursionlimit(10**6)
BUFSIZE = 4096
MOD = 10**9 + 7
MODD = 998244353

def solve():
    n, k = LII()
    p = LII()
    s = [0] + LII()
    d = defaultdict(list)
    for i in range(len(p)):
        d[p[i]].append(i+2)
    dp = {}
    @bootstrap
    def p(i, f):
        if (i, f) in dp:
            yield dp[i, f]
        ans = s[i] * f
        if not d[i]:
            yield ans
        if f % len(d[i]) == 0:
            for j in d[i]:
                ans += (yield p(j, f//len(d[i])))
        else:
            dp1, dp2 = [], []
            for j in d[i]:
                dp1.append((yield p(j, f//len(d[i]))))
                dp2.append((yield p(j, f//len(d[i])+1)))
            diff = sorted([j-i for i, j in zip(dp1, dp2)], reverse=True)
            ans += sum(dp1) + sum(diff[:f%len(d[i])])
        dp[i, f] = ans
        yield ans
    print(p(1, k))
    return

def main():
    for _ in range(II()):
        solve()

def bootstrap(f, stack=[]):
    from types import GeneratorType
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

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
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

if __name__ == "__main__":
    main()