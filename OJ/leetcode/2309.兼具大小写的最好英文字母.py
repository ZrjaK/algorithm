# 题目：2309.兼具大小写的最好英文字母
# 难度：EASY
# 最后提交：2022-06-19 10:31:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for i in range(97, 97+26):
            if chr(i) in s and chr(i).upper() in s:
                ans = chr(i).upper()
        return ans