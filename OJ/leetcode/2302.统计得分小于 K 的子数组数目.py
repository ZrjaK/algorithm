# 题目：2302.统计得分小于 K 的子数组数目
# 难度：HARD
# 最后提交：2022-06-11 23:48:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        h = list(accumulate(nums))
        n = len(nums)
        ans = 0
        for i in range(n):
            l, r = 1, i+1
            t = 0
            while l <= r:
                mid = l+r>>1
                f = h[i]-h[i-mid] if i-mid >= 0 else h[i]
                if mid * f < k:
                    t = mid
                    l = mid + 1
                else:
                    t = mid
                    r = mid - 1
            # f = h[i]-h[i-t] if i-t >= 0 else h[i]
            # if t <= i+1 and t * f < k:
                # print(t)
            ans += r
        # print()
        return ans
            