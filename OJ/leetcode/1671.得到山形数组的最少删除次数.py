# 题目：1671.得到山形数组的最少删除次数
# 难度：HARD
# 最后提交：2022-12-14 20:20:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        # 作为数组末尾前序最长的递增子序列长度
        dp = []
        pre = [0] * n
        for i in range(n):
            j = bisect.bisect_left(dp, nums[i])
            pre[i] = j
            if j == len(dp):
                dp.append(nums[i])
            else:
                dp[j] = nums[i]

        # 作为数组开头后序最长的递减子序列长度
        dp = []
        post = [0] * n
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(dp, nums[i])
            post[i] = j
            if j == len(dp):
                dp.append(nums[i])
            else:
                dp[j] = nums[i]
        
        # 遍历数组的山峰点，计算可以形成的最大山脉数组长度即可得到需要删除的最少次数
        ans = n
        for i in range(1, n - 1):
            # 注意山峰点的前提是左右两边都要有单调的非空子序列存在
            if pre[i] and post[i] and n - pre[i] - post[i] - 1 < ans:
                ans = n - pre[i] - post[i] - 1
        return ans
