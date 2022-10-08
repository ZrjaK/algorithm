# 题目：1754.构造字典序最大的合并字符串
# 难度：MEDIUM
# 最后提交：2022-06-13 15:24:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        a, b = word1, word2
        res = ""
        while a and b:
            if a > b:
                res += a[0]
                a = a[1:]
            else:
                res += b[0]
                b = b[1:]
        return res + a + b