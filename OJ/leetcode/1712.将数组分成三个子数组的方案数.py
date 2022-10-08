# 题目：1712.将数组分成三个子数组的方案数
# 难度：MEDIUM
# 最后提交：2022-05-09 15:16:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        pre = list(accumulate(nums))
        ans = 0
        for i in range(n):
            l = max(i+1,bisect_left(pre,pre[i]+pre[i]))
            r = min(n-1,bisect_right(pre,(pre[i]+pre[-1])//2))
            ans += max(0,r - l)
        return ans % int(1e9+7)