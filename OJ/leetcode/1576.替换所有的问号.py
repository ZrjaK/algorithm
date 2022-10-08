# 题目：1576.替换所有的问号
# 难度：EASY
# 最后提交：2021-10-20 11:15:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def modifyString(self, s: str) -> str:
        index = s.find("?")
        while index != -1:
            if s[index-1:index] != "a" and s[index+1:index+2] != "a":
                s = s[:index] + "a" + s[index+1:]
            if s[index-1:index] != "b" and s[index+1:index+2] != "b":
                s = s[:index] + "b" + s[index+1:]
            if s[index-1:index] != "c" and s[index+1:index+2] != "c":
                s = s[:index] + "c" + s[index+1:]
            index = s.find("?")
        return s