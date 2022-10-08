# 题目：1040.移动石子直到连续 II
# 难度：MEDIUM
# 最后提交：2022-06-09 16:28:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()
        maxans = stones[n-1]-stones[0]+1-n - min(stones[n-1]-stones[n-2]-1, stones[1]-stones[0] -1)
        minans = 1e99
        j = 0
        for i in range(n):
            while j+1 < n and stones[j+1] - stones[i] < n:
                j += 1
            t = n - (j-i+1)
            if j-i+1 == n-1 and stones[j] - stones[i] + 1 == n-1:
                t = 2
            minans = min(minans, t)
        return [minans, maxans]