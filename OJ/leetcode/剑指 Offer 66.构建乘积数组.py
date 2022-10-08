# 题目：剑指 Offer 66.构建乘积数组
# 难度：MEDIUM
# 最后提交：2022-10-03 21:16:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return a
        n = len(a)
        h1 = [a[0]]
        for i in range(1, n):
            h1.append(h1[-1] * a[i])
        h2 = [a[-1]]
        for i in range(n-2, -1, -1):
            h2.append(h2[-1] * a[i])
        h2 = h2[::-1]
        ans = [0] * n
        for i in range(1, n-1):
            ans[i] = h1[i-1] * h2[i+1]
        ans[0] = h2[1]
        ans[-1] = h1[-2]
        return ans
        