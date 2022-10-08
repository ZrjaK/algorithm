# 题目：1402.做菜顺序
# 难度：HARD
# 最后提交：2022-03-25 20:18:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        t = ans = 0
        for i in satisfaction:
            t += i
            if t < 0:
                break
            ans += t
        return ans