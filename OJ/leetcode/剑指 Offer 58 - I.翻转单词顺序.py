# 题目：剑指 Offer 58 - I.翻转单词顺序
# 难度：EASY
# 最后提交：2022-10-03 20:33:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.strip().split(" ") if i][::-1])