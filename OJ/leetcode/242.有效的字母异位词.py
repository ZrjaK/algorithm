# 题目：242.有效的字母异位词
# 难度：EASY
# 最后提交：2021-10-21 15:26:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)