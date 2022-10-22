import random
import sys
import os
import math
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
import threading
import bisect
from bisect import bisect_left, bisect_right, insort, insort_left, insort_right
# sys.setrecursionlimit(10**5)
BUFSIZE = 4096
MOD = 10**9 + 7
MODD = 998244353   

def solve():
    n = II()
    s = I()
    s = list(s.lstrip("0"))
    n = len(s)
    if not n:
        print("0")
        return
    h0 = []
    h1 = []
    for i in range(n):
        if s[i] == "0":
            h0.append(i)
        else:
            h1.append(i)
    def calc(x, j):
        res = []
        i = 0
        while i < len(h0) and j < len(h1):
            if h0[i] == h1[j]+x:
                res.append(h0[i])
                i += 1
                j += 1
            elif h0[i] < h1[j]+x:
                i += 1
            else:
                j += 1
        return res
    def compare(f1, f2):
        i = j = 0
        while i < len(f1) and j < len(f2):
            if f1[i] > f2[j]:
                return False
            elif f1[i] < f2[j]:
                return True
            else:
                i += 1
                j += 1
        if i < len(f1):
            return True
        return False
    res = [n] * n
    for i in range(len(h1)):
        if h1[i] > h0[0]:
            break
        t = calc(h0[0]-h1[i], i)
        if compare(t, res):
            res = t
    for i in res:
        s[i] = "1"
    print("".join(s))
    return

def main():
    for _ in range(1):
        solve()

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