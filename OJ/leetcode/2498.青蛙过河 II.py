# 题目：2498.青蛙过河 II
# 难度：MEDIUM
# 最后提交：2022-12-11 00:02:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        ans = stones[1] - stones[0]
        for i in range(2, n):
            ans = max(ans, stones[i] - stones[i-2])
        return ans
            
            
            