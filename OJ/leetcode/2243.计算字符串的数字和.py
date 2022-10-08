# 题目：2243.计算字符串的数字和
# 难度：EASY
# 最后提交：2022-04-17 10:34:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        ans = ""
        for i in range(0,len(s),k):
            t = s[i:i+k]
            a = 0
            for j in t:
                a += int(j)
            ans += str(a)
        return self.digitSum(ans,k)