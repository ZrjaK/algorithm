# 题目：171.Excel 表列序号
# 难度：EASY
# 最后提交：2022-11-01 16:15:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            ans += ord(i) - 65 + 1
            ans *= 26
        return ans // 26