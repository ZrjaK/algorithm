# 题目：1781.所有子字符串美丽值之和
# 难度：MEDIUM
# 最后提交：2022-12-12 15:11:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            c = defaultdict(int)
            for j in range(i, n):
                c[s[j]] += 1
                ans += max(c.values()) - min(c.values())
        return ans