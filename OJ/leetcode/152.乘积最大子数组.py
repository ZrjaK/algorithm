# 题目：152.乘积最大子数组
# 难度：MEDIUM
# 最后提交：2022-04-30 12:32:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B)) 