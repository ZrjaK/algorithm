# 题目：2287.重排字符形成目标字符串
# 难度：EASY
# 最后提交：2023-01-13 00:19:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        return min([c[i] // target.count(i) for i in target])