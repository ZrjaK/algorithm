# 题目：剑指 Offer II 005.单词长度的最大乘积
# 难度：MEDIUM
# 最后提交：2022-10-04 10:20:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        h = []
        for i in words:
            t = 0
            for j in i:
                t |= 1<<ord(j)-97
            h.append(t)
        n = len(h)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if not h[i] & h[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans