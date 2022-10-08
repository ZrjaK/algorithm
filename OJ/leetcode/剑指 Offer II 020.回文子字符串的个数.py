# 题目：剑指 Offer II 020.回文子字符串的个数
# 难度：MEDIUM
# 最后提交：2022-10-05 14:54:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        res = n
        for l in range(n-1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    if r - l == 1:
                        dp[l][r] = True
                        res += 1    
                    else:
                        if dp[l+1][r-1] == True:
                            dp[l][r] = True
                            res += 1
        return res