# 题目：58.最后一个单词的长度
# 难度：EASY
# 最后提交：2021-10-20 19:44:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])