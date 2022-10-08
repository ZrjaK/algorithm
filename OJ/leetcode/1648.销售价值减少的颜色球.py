# 题目：1648.销售价值减少的颜色球
# 难度：MEDIUM
# 最后提交：2022-05-09 12:09:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        n = len(inventory)
        l, r = 0, max(inventory)
        while l <= r:
            mid = l+r>>1
            t = sum([max(0, i-mid) for i in inventory])
            if t <= orders:
                r = mid - 1
            else:
                l = mid + 1
        ans = 0
        for i in inventory:
            t = max(0, i-l)
            if t:
                ans += (i+l+1) * t // 2
            orders -= t
        ans += orders * l
        return ans % int(1e9+7)