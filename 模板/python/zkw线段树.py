class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    # return smallest i(l <= i < r) s.t. check(A[i]) == True
    def binsearch(self, l, r, check):
        if not check(self.query(l, r)):
            return r
        l += self.num
        val = self.ide_ele
        while 1:
            if check(self.segfunc(val, self.tree[l])):
                break
            if l & 1:
                val = self.segfunc(val, self.tree[l])
                l += 1
            l >>= 1
        while l < self.num:
            newval = self.segfunc(val, self.tree[l << 1])
            if not check(newval):
                val = newval
                l = (l << 1) + 1
            else:
                l <<= 1
        return l - self.num