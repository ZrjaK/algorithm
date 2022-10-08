# 题目：2064.分配给商店的最多商品的最小值
# 难度：MEDIUM
# 最后提交：2022-05-18 22:52:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, int(1e5)
        while l <= r:
            mid = l+r>>1
            s = 0
            for i in quantities:
                s += i // mid
                if i % mid != 0:
                    s += 1
            if s <= n:
                r = mid - 1
            else:
                l = mid + 1
        return l