# 题目：168.Excel表列名称
# 难度：EASY
# 最后提交：2022-11-01 12:46:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return ans[::-1]