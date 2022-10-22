# 题目：2286.以组为单位订音乐会的门票
# 难度：HARD
# 最后提交：2022-10-18 20:46:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.st = SegmentTree()

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.st.index(self.st.root, 0, self.n, 0, maxRow, self.m-k)
        if i == -1:
            return []
        seats = self.st.query(self.st.root, 0, self.n, i, i)
        self.st.add(self.st.root, 0, self.n, i, i, k)
        return [i, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow+1) * self.m - self.st.query(self.st.root, 0, self.n, 0, maxRow) < k:
            return False
        i = self.st.index(self.st.root, 0, self.n, 0, maxRow, self.m-1)
        if i == -1:
            return False
        while 1:
            left_seats = self.m - self.st.query(self.st.root, 0, self.n, i, i)
            if k <= left_seats:
                self.st.add(self.st.root, 0, self.n, i, i, k)
                return True
            k -= left_seats
            self.st.add(self.st.root, 0, self.n, i, i, left_seats)
            i += 1


class STNode:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        self.left = left
        self.right = right
        self.val = val
        self.min_ = 0
        self.lazy = lazy

class SegmentTree:
    def __init__(self):
        self.root = STNode()
    
    def add(self, node, l, r, start, end, x):
        if l == start and r == end:
            node.lazy += x
            return
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            self.add(node.left, l, mid, start, end, x)
        elif start > mid:
            self.add(node.right, mid+1, r, start, end, x)
        else:
            self.add(node.left, l, mid, start, mid, x)
            self.add(node.right, mid+1, r, mid+1, end, x)
        self.pushup(node, mid-l+1, r-mid)

    def query(self, node, l, r, start, end):
        if l == start and r == end:
            return node.lazy * (r-l+1) + node.val
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            res = self.query(node.left, l, mid, start, end)
        elif start > mid:
            res = self.query(node.right, mid+1, r, start, end)
        else:
            res = self.query(node.left, l, mid, start, mid) + \
                self.query(node.right, mid+1, r, mid+1, end)
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def index(self, node, l, r, start, end, val):
        if node.min_ + node.lazy > val:
            return -1
        if l == r:
            return l
        mid = l+r>>1
        self.pushdown(node)
        if node.left.min_ + node.left.lazy <= val:
            return self.index(node.left, l, mid, start, end, val)
        elif mid < end:
            return self.index(node.right, mid+1, r, start, end, val)
        self.pushup(node, mid-l+1, r-mid)
        return -1
    
    def pushdown(self, node):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.lazy:
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0
    
    def pushup(self, node, ln, rn):
        node.val = node.left.val + node.right.val + node.left.lazy * ln + node.right.lazy * rn
        node.min_ = min(node.left.min_+node.left.lazy, node.right.min_+node.right.lazy)

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)