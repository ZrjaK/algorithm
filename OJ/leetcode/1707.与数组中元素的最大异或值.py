# 题目：1707.与数组中元素的最大异或值
# 难度：HARD
# 最后提交：2022-09-30 09:25:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(list(set(nums)), reverse=True)
        n = len(nums)
        h = [set() for _ in range(32)]
        queries = [[i, j, k] for i, (j, k) in enumerate(queries)]
        ans = [-1] * len(queries)
        queries.sort(key=lambda x: x[2])
        trie = Trie()
        for i, j, k in queries:
            while nums and nums[-1] <= k:
                trie.insert(nums.pop())
            if len(nums) != n:
                ans[i] = trie.getMaxXor(j)
        return ans
                    
class Trie:
    def __init__(self):
        self.left = None
        self.right = None
    
    def insert(self, x):
        node = self
        for i in range(31, -1, -1):
            if x>>i & 1:
                if not node.right:
                    node.right = Trie()
                node = node.right
            else:
                if not node.left:
                    node.left = Trie()
                node = node.left
            
    def getMaxXor(self, x):
        res = 0
        node = self
        for i in range(31, -1, -1):
            f = False
            if x>>i & 1:
                if node.left:
                    f = True
                    node = node.left
                else:
                    node = node.right
            else:
                if node.right:
                    f = True
                    node = node.right
                else:
                    node = node.left
            if f:
                res |= 1<<i
        return res