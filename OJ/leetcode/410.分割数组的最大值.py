# 题目：410.分割数组的最大值
# 难度：HARD
# 最后提交：2022-04-14 11:25:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l , r = max(nums), sum(nums)
        while l < r:
            mid = l+r >> 1
            s = 0
            cnt = 1
            for i in nums:
                s += i
                if s > mid:
                    cnt += 1
                    s = i
            if cnt > m:
                l = mid + 1
            else:
                r = mid
        return l