# 题目：28.找出字符串中第一个匹配项的下标
# 难度：MEDIUM
# 最后提交：2021-10-20 17:04:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)