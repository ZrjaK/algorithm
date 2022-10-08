# 题目：1839.所有元音按顺序排布的最长子字符串
# 难度：MEDIUM
# 最后提交：2022-05-25 11:35:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 0
        t = 1
        l = 0
        for r in range(1, len(word)):
            if word[r] < word[r-1]:
                l = r
                t = 1
            elif word[r] > word[r-1]:
                t += 1
            if t == 5:
                ans = max(ans, r-l+1)
        return ans