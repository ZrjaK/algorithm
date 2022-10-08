# 题目：2278.字母在字符串中的百分比
# 难度：EASY
# 最后提交：2022-05-22 10:31:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0
        for i in s:
            if i == letter:
                c += 1
        return  c*100//len(s)