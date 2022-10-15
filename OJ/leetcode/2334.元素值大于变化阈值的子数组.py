# 题目：2334.元素值大于变化阈值的子数组
# 难度：HARD
# 最后提交：2022-10-13 13:08:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        q = [-1]
        for i in range(n+1):
            while q[-1] != -1 and (i == n or nums[q[-1]] >= nums[i]):
                t = q.pop()
                if (i-q[-1]-1) * nums[t] > threshold:
                    return i-q[-1]-1
            q.append(i)
        return -1