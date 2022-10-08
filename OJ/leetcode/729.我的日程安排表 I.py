# 题目：729.我的日程安排表 I
# 难度：MEDIUM
# 最后提交：2022-08-23 03:03:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MyCalendar:

    def __init__(self):
        self.st = SegmentTree()

    def book(self, start: int, end: int) -> bool:
        if self.st.querySum(self.st.root, 0, 10**9, start, end-1):
            return False
        self.st.add(self.st.root, 0, 10**9, start, end-1, 1)
        return True

class STNode:
    def __init__(self, left=None, right=None, val=0, add=0):
        self.left = left
        self.right = right
        self.val = val
        self.add = add

class SegmentTree:
    def __init__(self):
        self.root = STNode()
    
    def add(self, node, l, r, start, end, x):
        if l == start and r == end:
            node.add += x
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

    def querySum(self, node, l, r, start, end):
        if l == start and r == end:
            return node.add * (r-l+1) + node.val
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            res = self.querySum(node.left, l, mid, start, end)
        elif start > mid:
            res = self.querySum(node.right, mid+1, r, start, end)
        else:
            res = self.querySum(node.left, l, mid, start, mid) + self.querySum(node.right, mid+1, r, mid+1, end)
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def pushdown(self, node):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.add:
            node.left.add += node.add
            node.right.add += node.add
            node.add = 0
    
    def pushup(self, node, ln, rn):
        node.val = node.left.val + node.right.val + node.left.add * ln + node.right.add * rn

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)