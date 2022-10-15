# 题目：剑指 Offer II 096.字符串交织
# 难度：MEDIUM
# 最后提交：2022-10-09 19:50:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def p(i, j, k):
            if k == len(s3):
                return True
            if i < len(s1) and s1[i] == s3[k] and p(i+1, j, k+1):
                return True
            if j < len(s2) and s2[j] == s3[k] and p(i, j+1, k+1):
                return True
            return False
        return p(0, 0, 0)