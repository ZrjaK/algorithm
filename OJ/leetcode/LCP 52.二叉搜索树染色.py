# 题目：LCP 52.二叉搜索树染色
# 难度：MEDIUM
# 最后提交：2022-12-30 01:04:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sortedcontainers import SortedList
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        odt = ODT()
        for t, x, y in ops:
            odt.assign(x, y+1, t)
        ans = 0
        def p(node):
            if not node:
                return
            nonlocal ans
            odt.split(node.val)
            ans += odt.mp[node.val]
            p(node.left)
            p(node.right)
        p(root)
        return ans

            
class ODT:
    def __init__(self):
        self.mp = {-1: 0}
        self.sl = SortedList([-1])

    def split(self, x):
        mp, sl = self.mp, self.sl
        pos = sl.bisect_right(x) - 1 # 找到左端点小于等于x的区间
        mp[x] = mp[sl[pos]] # 设立新的区间，并将上一个区间储存的值复制给本区间。
        if not sl.count(x):
            sl.add(x)

    def assign(self, l, r, v):
        mp, sl = self.mp, self.sl
        self.split(l)
        self.split(r)
        pos = sl.bisect_left(l)
        while sl[pos] != r:
            sl.pop(pos)
        mp[l] = v
        if not sl.count(l):
            sl.add(l)

    def update(self, l, r, v):
        mp, sl = self.mp, self.sl
        self.split(l)
        self.split(r)
        pos = sl.bisect_left(l)
        while sl[pos] != r:
            pos += 1