# 题目：1684.统计一致字符串的数目
# 难度：EASY
# 最后提交：2022-04-10 06:57:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for i in words:
            if set(i).issubset(allowed):
                ans += 1
        return ans