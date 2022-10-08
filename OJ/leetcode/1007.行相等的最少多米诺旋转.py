# 题目：1007.行相等的最少多米诺旋转
# 难度：MEDIUM
# 最后提交：2022-09-06 23:32:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = 1e99
        for x in range(1, 7):
            t = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    t = 1e99
                    break
                elif tops[i] != x:
                    t += 1
            if t < n:
                ans = min(ans, t, n-t)
        for x in range(1, 7):
            t = 0
            for i in range(n):
                if bottoms[i] != x and tops[i] != x:
                    t = 1e99
                    break
                elif bottoms[i] != x:
                    t += 1
            if t < n:
                ans = min(ans, t, n-t)
        return ans if ans < 1e90 else -1