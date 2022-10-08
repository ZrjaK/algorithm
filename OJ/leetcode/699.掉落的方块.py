# 题目：699.掉落的方块
# 难度：HARD
# 最后提交：2022-08-23 17:52:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        st = SegmentTree()
        ans = []
        for l, h in positions:
            c = st.query(st.root, 1, 10**9, l, l+h-1)
            st.add(st.root, 1, 10**9, l, l+h-1, c+h)
            ans.append(st.root.val)
        return ans

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
            node.val = x
            node.add = x
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
            return node.val
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            res = self.query(node.left, l, mid, start, end)
        elif start > mid:
            res = self.query(node.right, mid+1, r, start, end)
        else:
            res = max(self.query(node.left, l, mid, start, mid),
                self.query(node.right, mid+1, r, mid+1, end))
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def pushdown(self, node):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.add:
            node.left.val = node.add
            node.right.val = node.add
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0
    
    def pushup(self, node, ln, rn):
        node.val = max(node.left.val, node.right.val)
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)