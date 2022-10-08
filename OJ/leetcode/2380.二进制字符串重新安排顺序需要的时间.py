# 题目：2380.二进制字符串重新安排顺序需要的时间
# 难度：MEDIUM
# 最后提交：2022-08-20 22:34:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while "01" in s:
            s = s.replace("01", "10")
            ans += 1
        return ans