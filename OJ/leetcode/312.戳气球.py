# 题目：312.戳气球
# 难度：HARD
# 最后提交：2022-04-07 13:32:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def process(l, r):
            if l == r:
                return nums[l-1]*nums[l]*nums[r+1]
            res = max(nums[l-1]*nums[l]*nums[r+1] + process(l+1, r),
                      nums[l-1]*nums[r]*nums[r+1] + process(l, r-1))
            for i in range(l+1, r):
                res = max(res, nums[l-1]*nums[i]*nums[r+1]+process(l, i-1)+process(i+1,r))
            return res
        nums.insert(0, 1)
        nums.append(1)
        return process(1, len(nums)-2)