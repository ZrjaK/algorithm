# 题目：551.学生出勤记录 I
# 难度：EASY
# 最后提交：2021-10-22 19:15:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count('A') >= 2 or "LLL" in s)