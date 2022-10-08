# 题目：20.有效的括号
# 难度：EASY
# 最后提交：2022-09-04 17:00:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""