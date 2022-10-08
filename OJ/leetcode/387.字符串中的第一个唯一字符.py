# 题目：387.字符串中的第一个唯一字符
# 难度：EASY
# 最后提交：2021-10-21 19:44:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.find(i) == s.rfind(i):
                return s.index(i)
        return -1
                