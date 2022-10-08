# 题目：2063.所有子字符串中的元音
# 难度：MEDIUM
# 最后提交：2022-07-23 01:28:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countVowels(self, word: str) -> int:
        y = {"a", "e", "i", "o", "u"}
        n = len(word)
        dp = [0] * n + [0]
        for i in range(n):
            if word[i] in y:
                dp[i] = dp[i-1] + i + 1
            else:
                dp[i] = dp[i-1]
        return sum(dp)