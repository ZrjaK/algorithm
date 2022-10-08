# 题目：541.反转字符串 II
# 难度：EASY
# 最后提交：2022-05-01 20:06:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0,len(s), 2*k):
            ans += s[i:i+k][::-1] + s[i+k:i+2*k]
        return ans