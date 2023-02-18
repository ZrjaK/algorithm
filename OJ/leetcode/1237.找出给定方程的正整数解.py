# 题目：1237.找出给定方程的正整数解
# 难度：MEDIUM
# 最后提交：2023-02-18 00:40:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for i in range(1,1001):
            l, r = 1, 1000
            while l <= r:
                mid = l+r>>1
                t = customfunction.f(i, mid)
                if t == z:
                    res.append([i, mid])
                    break
                elif t < z:
                    l = mid + 1
                else:
                    r = mid - 1
        return res