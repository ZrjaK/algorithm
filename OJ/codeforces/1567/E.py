import sys

class SegTree:
 
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        # self.tree = [ide_ele] * 2 * self.num
        self.tree = ffi.new("node_t[]", 2 * self.num + 3)
        for i in range(2 * self.num):
            self.tree[i] = tnode
        for i in range(n):
            self.tree[self.num + i] = p(init_val[i])
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
 
    def update(self, k, x):
        k += self.num
        self.tree[k] = x

        k >>= 1
        # while k > 1:
        #     self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
        #     k >>= 1
        while k:
            self.tree[k] = self.segfunc(self.tree[k<<1], self.tree[k<<1|1])
            k >>= 1
 
    def query(self, l, r):
        # res = self.ide_ele
        self.tree[2 * self.num+1] = tnode
        self.tree[2 * self.num+2] = tnode
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                # res = self.segfunc(res, self.tree[l])
                self.tree[2 * self.num+1] = self.segfunc(self.tree[2 * self.num+1], self.tree[l])
                l += 1
            if r & 1:
                # res = self.segfunc(res, self.tree[r - 1])
                self.tree[2 * self.num+2] = self.segfunc(self.tree[r - 1], self.tree[2 * self.num+2]
)
            l >>= 1
            r >>= 1
        # return res
        self.tree[2 * self.num+1] = self.segfunc(self.tree[2 * self.num+1], self.tree[2 * self.num+2])
        return self.tree[2 * self.num+1]

def calc(l):
    return l * (l+1) // 2
from cffi import FFI
ffi = FFI()
ffi.cdef(
    """
    typedef struct {
        int lv;
        int rv;
        int ll;
        int rl;
        long long c;
        int b;
    } node_t;
    """
)
tdata = ffi.new("node_t[]", 1)
tdata[0] = (0, 0, 0, 0, 0, 0)
tnode = tdata[0]

def p(x):
    return (x, x, 1, 1, 0, 0)
def f(a, b):
    if not a.ll: return b
    if not b.ll: return a
    alv, arv, all, arl, ac, ab = a.lv, a.rv, a.ll, a.rl, a.c, a.b
    blv, brv, bll, brl, bc, bb = b.lv, b.rv, b.ll, b.rl, b.c, b.b
    clv, crv, cll, crl, cc, cb = alv, brv, all, brl, ac + bc, ab | bb
    if ab and bb:
        if arv <= blv: cc += calc(arl + bll)
        else: cc += calc(arl) + calc(bll)
    elif ab and not bb:
        if arv <= blv: crl += arl
        else: cc += calc(arl)
    elif not ab and bb:
        if arv <= blv: cll += bll
        else: cc += calc(bll)
    else:
        if arv <= blv: cll = crl = all + bll
        else: cb = 1
    return (clv, crv, cll, crl, cc, cb)
def solve():
    n, q = LII()
    arr = LII()
    seg = SegTree(arr, f, tnode)
    aans = []
    for _ in range(q):
        op, l, r = LII()
        if op == 1:
            seg.update(l-1, p(r))
        else:
            res = seg.query(l-1, r)
            lv, rv, ll, rl, c, b = res.lv, res.rv, res.ll, res.rl, res.c, res.b
            if b: ans = c + calc(ll) + calc(rl)
            else: ans = calc(ll)
            aans.append(ans)
    print(*aans, sep='\n')


def main():
    t = 1
    # t = II()
    for _ in range(t):
        solve()

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

def debug(*args):
    print('\033[92m', end='')
    print(*args)
    print('\033[0m', end='')

if __name__ == "__main__":
    main()