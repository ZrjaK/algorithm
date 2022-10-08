# 题目：907.子数组的最小值之和
# 难度：MEDIUM
# 最后提交：2022-07-08 17:04:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A.append(-1)
        stack, res= [-1], 0
        for i in range(len(A)):
            while A[i] < A[stack[-1]]:
                idx = stack.pop()
                res += A[idx] * (i-idx) * (idx-stack[-1])
            stack.append(i)
        return res % int(1e9+7)