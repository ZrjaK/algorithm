# 题目：2525.根据规则将箱子分类
# 难度：EASY
# 最后提交：2023-01-07 22:32:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        h = []
        if any([i >= 10**4 for i in [length, width, height, mass]]) or length * width * height >= 10**9:
            h.append("Bulky")
        if mass >= 100:
            h.append("Heavy")
        if len(h) == 2:
            return "Both"
        if not h:
            return "Neither"
        return h[0]
        