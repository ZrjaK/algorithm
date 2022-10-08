# 题目：557.反转字符串中的单词 III
# 难度：EASY
# 最后提交：2021-10-22 19:17:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())