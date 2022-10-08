# 题目：904.水果成篮
# 难度：MEDIUM
# 最后提交：2022-05-21 00:55:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = r = ans = 0
        b1 = b2 = fruits[0]
        while r < n:
            if fruits[r] == b1 or fruits[r] == b2:
                ans = max(ans, r - l + 1)
                r += 1
            else:
                l = r - 1
                b1 = fruits[l]
                while l >= 1 and fruits[l-1] == b1:
                    l -= 1
                b2 = fruits[r]
                ans = max(ans, r - l + 1)
        return ans