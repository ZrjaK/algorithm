# 题目：2315.统计星号
# 难度：EASY
# 最后提交：2023-01-29 00:11:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split("|")
        ans = 0
        for i in range(0, len(l), 2):
            ans += l[i].count("*")
        return ans