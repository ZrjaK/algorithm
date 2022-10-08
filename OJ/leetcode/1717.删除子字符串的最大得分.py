# 题目：1717.删除子字符串的最大得分
# 难度：MEDIUM
# 最后提交：2022-04-12 02:46:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        i = 0
        if x >= y:
            while i < len(s):
                while s[i:i+2] == "ab":
                    ans += x
                    s = s[:i] + s[i+2:]
                    i = max(0, i-1)
                i += 1
            i = 0
            while i < len(s):
                while s[i:i+2] == "ba":
                    ans += y
                    s = s[:i] + s[i+2:]
                    i = max(0, i-1)
                i += 1
        else:
            while i < len(s):
                while s[i:i+2] == "ba":
                    ans += y
                    s = s[:i] + s[i+2:]
                    i = max(0, i-1)
                i += 1
            i = 0
            while i < len(s):
                while s[i:i+2] == "ab":
                    ans += x
                    s = s[:i] + s[i+2:]
                    i = max(0, i-1)
                i += 1
        return ans
        