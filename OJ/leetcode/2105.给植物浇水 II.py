# 题目：2105.给植物浇水 II
# 难度：MEDIUM
# 最后提交：2022-06-21 13:00:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants) - 1
        a, b = capacityA, capacityB
        ans = 0
        while l < r:
            if a < plants[l]:
                ans += 1
                a = capacityA
            a = a - plants[l]
            l += 1
            if b < plants[r]:
                ans += 1
                b = capacityB
            b = b - plants[r]
            r -= 1
        if l == r:
            if a >= b:
                if a < plants[l]:
                    ans += 1
            else:
                if b < plants[r]:
                    ans += 1
        return ans