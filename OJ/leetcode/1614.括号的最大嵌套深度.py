# 题目：1614.括号的最大嵌套深度
# 难度：EASY
# 最后提交：2021-10-20 12:50:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDepth(self, s: str) -> int:
        maxdep = 0
        for i in range(len(s)):
            if s[i:i+1] == "(" or i == ")":
                continue
            temp = 0
            for j in s[:i]:
                if j == "(":
                    temp +=1
                if j == ")":
                    temp -= 1
            maxdep = max(maxdep, temp)
        return maxdep

                
                
            