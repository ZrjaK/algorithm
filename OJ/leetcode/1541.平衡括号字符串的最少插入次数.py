# 题目：1541.平衡括号字符串的最少插入次数
# 难度：MEDIUM
# 最后提交：2022-09-04 23:22:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minInsertions(self, s: str) -> int:
        ans = l = 0
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            if s[i] == "(":
                l +=1
            else:
                if i+1 < n and s[i+1] == ")":
                    i += 1
                else:
                    ans += 1
                if l:
                    l -= 1
                else:
                    ans += 1
            i += 1
        ans += l * 2
        return ans