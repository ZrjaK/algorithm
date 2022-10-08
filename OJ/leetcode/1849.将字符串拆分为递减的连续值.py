# 题目：1849.将字符串拆分为递减的连续值
# 难度：MEDIUM
# 最后提交：2022-09-14 13:42:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def p(i, k):
            if i == n:
                return True
            for j in range(i+1, n+1):
                if int(s[i:j]) == k-1 and p(j, k-1):
                    return True
            return False
        for i in range(1, n):
            if p(i, int(s[:i])):
                return True
        return False