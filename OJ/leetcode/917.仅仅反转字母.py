# 题目：917.仅仅反转字母
# 难度：EASY
# 最后提交：2021-11-02 18:52:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        p = [i for i in s if i.isalpha()]
        return ''.join([i if not i.isalpha() else p.pop() for i in s])