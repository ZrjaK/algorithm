# 题目：1673.找出最具竞争力的子序列
# 难度：MEDIUM
# 最后提交：2022-09-04 23:42:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        c = n-k
        for i in nums:
            while stack and c and stack[-1] > i:
                stack.pop()
                c -= 1
            stack.append(i)
        return stack[:k]