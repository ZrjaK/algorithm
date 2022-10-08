# 题目：2405.子字符串的最优划分
# 难度：MEDIUM
# 最后提交：2022-09-11 10:33:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partitionString(self, s: str) -> int:
        c = [0] * 26
        ans = 0
        for i in s:
            c[ord(i)-97] += 1
            if not all([i <= 1 for i in c]):
                ans += 1
                c = [0] * 26
                c[ord(i)-97] += 1
        return ans + 1