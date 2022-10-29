# 题目：1768.交替合并字符串
# 难度：EASY
# 最后提交：2022-10-23 00:26:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        ans += word1[i:] + word2[j:]
        return ans