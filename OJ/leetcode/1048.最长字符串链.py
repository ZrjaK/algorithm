# 题目：1048.最长字符串链
# 难度：MEDIUM
# 最后提交：2022-06-09 17:27:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())