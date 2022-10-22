# 题目：1622.奇妙序列
# 难度：HARD
# 最后提交：2022-10-19 11:37:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Fancy:

    def __init__(self):
        self.st = SegmentTree()
        self.a = -1

    def append(self, val: int) -> None:
        self.a += 1
        self.st.add(self.st.root, 0, 10**5, self.a, self.a, val)

    def addAll(self, inc: int) -> None:
        if self.a < 0:
            return
        self.st.add(self.st.root, 0, 10**5, 0, self.a, inc)
        # print("add", [self.st.query(self.st.root, 0, 10**5, i, i) for i in range(len(self.arr))])
    def multAll(self, m: int) -> None:
        if self.a < 0:
            return
        self.st.multi(self.st.root, 0, 10**5, 0, self.a, m)
        # print("mul", [self.st.query(self.st.root, 0, 10**5, i, i) for i in range(len(self.arr))])

    def getIndex(self, idx: int) -> int:
        if idx > self.a:
            return -1
        return self.st.query(self.st.root, 0, 10**5, idx, idx)


class STNode:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy
        self.mlazy = 1

class SegmentTree:
    def __init__(self):
        self.root = STNode()
    
    def add(self, node, l, r, start, end, x):
        if l == start and r == end:
            node.lazy += x
            return
        mid = l+r>>1
        self.pushdown(node, mid-l+1, r-mid)
        if end <= mid:
            self.add(node.left, l, mid, start, end, x)
        elif start > mid:
            self.add(node.right, mid+1, r, start, end, x)
        else:
            self.add(node.left, l, mid, start, mid, x)
            self.add(node.right, mid+1, r, mid+1, end, x)
        self.pushup(node, mid-l+1, r-mid)
    
    def multi(self, node, l, r, start, end, x):
        if l == start and r == end:
            node.mlazy *= x
            node.lazy *= x
            node.val *= x
            return
        mid = l+r>>1
        self.pushdown(node, mid-l+1, r-mid)
        if end <= mid:
            self.multi(node.left, l, mid, start, end, x)
        elif start > mid:
            self.multi(node.right, mid+1, r, start, end, x)
        else:
            self.multi(node.left, l, mid, start, mid, x)
            self.multi(node.right, mid+1, r, mid+1, end, x)
        self.pushup(node, mid-l+1, r-mid)

    def query(self, node, l, r, start, end):
        if l == start and r == end:
            return node.lazy * (r-l+1) + node.val
        mid = l+r>>1
        self.pushdown(node, mid-l+1, r-mid)
        if end <= mid:
            res = self.query(node.left, l, mid, start, end)
        elif start > mid:
            res = self.query(node.right, mid+1, r, start, end)
        else:
            res = self.query(node.left, l, mid, start, mid) + \
                self.query(node.right, mid+1, r, mid+1, end)
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def pushdown(self, node, ln, rn):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.lazy == 0 and node.mlazy == 1:
            return
        node.left.lazy = node.lazy + node.left.lazy * node.mlazy
        node.right.lazy = node.lazy + node.right.lazy * node.mlazy
        node.left.mlazy *= node.mlazy
        node.right.mlazy *= node.mlazy
        node.left.lazy %= int(1e9+7)
        node.right.lazy %= int(1e9+7)
        node.left.mlazy %= int(1e9+7)
        node.right.mlazy %= int(1e9+7)
        node.lazy = 0
        node.mlazy = 1
    
    def pushup(self, node, ln, rn):
        node.val = node.left.val + node.right.val + node.left.lazy * ln + node.right.lazy * rn
        node.val %= int(1e9+7)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)