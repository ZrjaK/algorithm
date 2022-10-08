# 题目：875.爱吃香蕉的珂珂
# 难度：MEDIUM
# 最后提交：2022-05-03 10:15:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = l+r>>1
            t = 0
            for i in piles:
                t += i // mid
                if i % mid != 0:
                    t += 1
            if t > h:
                l = mid + 1
            else:
                r = mid - 1
        return l