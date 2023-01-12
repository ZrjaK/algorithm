# 题目：2185.统计包含给定前缀的字符串
# 难度：EASY
# 最后提交：2023-01-08 00:15:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([i for i in words if i.startswith(pref)])