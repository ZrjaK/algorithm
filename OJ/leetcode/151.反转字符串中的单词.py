# 题目：151.反转字符串中的单词
# 难度：MEDIUM
# 最后提交：2022-05-30 21:51:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.split(" ")[::-1] if i != ""])