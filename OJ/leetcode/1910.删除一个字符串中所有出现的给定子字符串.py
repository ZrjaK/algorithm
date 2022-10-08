# 题目：1910.删除一个字符串中所有出现的给定子字符串
# 难度：MEDIUM
# 最后提交：2022-03-25 17:42:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        t = ""
        for i in s:
            t += i
            while len(t) >= len(part) and t[-len(part):] == part:
                t = t[:-len(part)]
        return t