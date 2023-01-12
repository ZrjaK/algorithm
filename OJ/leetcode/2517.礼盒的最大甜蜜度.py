# 题目：2517.礼盒的最大甜蜜度
# 难度：MEDIUM
# 最后提交：2022-12-25 19:05:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l, r = -1, 10**18
        while l + 1 < r:
            mid = l+r>>1
            h = []
            for i in price:
                if not h:
                    h.append(i)
                elif i - h[-1] >= mid:
                    h.append(i)
            if len(h) >= k:
                l = mid
            else:
                r = mid
        return l