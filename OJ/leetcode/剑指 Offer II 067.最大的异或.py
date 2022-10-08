# 题目：剑指 Offer II 067.最大的异或
# 难度：MEDIUM
# 最后提交：2022-10-08 12:31:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        trie = Trie()
        for i in nums:
            trie.insert(i)
            ans = max(ans, trie.getMaxXor(i))
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