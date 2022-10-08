# 题目：1011.在 D 天内送达包裹的能力
# 难度：MEDIUM
# 最后提交：2022-04-13 07:03:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l+r>>1
            t = 0
            day = 1
            for w in weights:
                t += w
                if t > mid:
                    t = w
                    day += 1
            if day > days:
                l = mid + 1
            else:
                r = mid
        return l