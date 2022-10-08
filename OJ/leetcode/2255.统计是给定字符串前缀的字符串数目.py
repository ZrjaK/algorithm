# 题目：2255.统计是给定字符串前缀的字符串数目
# 难度：EASY
# 最后提交：2022-04-30 22:37:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for i in words:
            if i == s[:len(i)]:
                ans += 1
        return ans