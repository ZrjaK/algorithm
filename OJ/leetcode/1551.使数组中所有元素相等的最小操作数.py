# 题目：1551.使数组中所有元素相等的最小操作数
# 难度：MEDIUM
# 最后提交：2022-05-07 16:40:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n+n%2+1, 2*n+1, 2):
            ans += i-n
        return ans