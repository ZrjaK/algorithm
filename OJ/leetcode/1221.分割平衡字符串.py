# 题目：1221.分割平衡字符串
# 难度：EASY
# 最后提交：2022-09-05 15:45:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = ans = 0
        for i in s:
            if i == "L":
                l += 1
            else:
                r += 1
            if l == r:
                ans += 1
        return ans