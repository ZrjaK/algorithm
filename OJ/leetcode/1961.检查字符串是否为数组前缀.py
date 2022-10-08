# 题目：1961.检查字符串是否为数组前缀
# 难度：EASY
# 最后提交：2022-09-06 08:29:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for k in range(len(words)):
            if "".join(words[:k+1]) == s:
                return True
        return False