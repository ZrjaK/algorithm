# 题目：1915.最美子字符串的数目
# 难度：MEDIUM
# 最后提交：2022-08-27 01:32:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        t = 0
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for s in word:
            t ^= 1<<ord(s)-97
            ans += d[t]
            for i in range(26):
                ans += d[t ^ 1<<i]
            d[t] += 1
        return ans