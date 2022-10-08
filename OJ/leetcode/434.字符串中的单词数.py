# 题目：434.字符串中的单词数
# 难度：EASY
# 最后提交：2021-10-21 23:55:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())