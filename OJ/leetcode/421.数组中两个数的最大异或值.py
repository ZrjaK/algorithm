# 题目：421.数组中两个数的最大异或值
# 难度：MEDIUM
# 最后提交：2022-08-25 16:27:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = max(len(bin(i)) for i in nums) - 2
        root = Trie(-1)
        for i in nums:
            t = root
            for j in range(L-1, -1, -1):
                v = i>>j & 1
                if v not in t.child:
                    t.child[v] = Trie(v)
                t = t.child[v]
        ans = 0
        for i in nums:
            t = root
            c = 0
            for j in range(L-1, -1, -1):
                v = i>>j & 1
                if v^1 in t.child:
                    c |= 1<<j
                    t = t.child[v^1]
                else:
                    t = t.child[v]
            ans = max(ans, c)
        return ans

                

class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}
