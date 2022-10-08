# 题目：2407.最长递增子序列 II
# 难度：HARD
# 最后提交：2022-09-11 11:35:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [1] * n
        st = SegmentTree()
        ma = max(nums)
        for i in range(n):
            dp[i] = 1 + st.query(st.root, 0, ma, max(nums[i]-k, 0), max(nums[i]-1, 0))
            f = st.query(st.root, 0, ma, nums[i], nums[i])
            # print(i, f)
            if dp[i] > f:
                st.add(st.root, 0, ma, nums[i], nums[i], dp[i])
        # print(dp)
        return max(dp)
    

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
            return node.add+node.val
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            res = self.query(node.left, l, mid, start, end)
        elif start > mid:
            res = self.query(node.right, mid+1, r, start, end)
        else:
            res = max(self.query(node.left, l, mid, start, mid) ,
                self.query(node.right, mid+1, r, mid+1, end))
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def pushdown(self, node):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.add:
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0
    
    def pushup(self, node, ln, rn):
        node.val = max(node.left.val+node.left.add, node.right.val+node.right.add)