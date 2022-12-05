# 题目：2486.追加字符以获得子序列
# 难度：MEDIUM
# 最后提交：2022-11-27 12:24:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = 0
        j = 0
        for i in s:
            if j < len(t) and i == t[j]:
                ans += 1
                j += 1
        return len(t) - ans