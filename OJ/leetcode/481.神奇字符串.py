# 题目：481.神奇字符串
# 难度：MEDIUM
# 最后提交：2022-06-02 23:00:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        pre, now = 2, 2
        while now < n:
            t = int(s[pre])
            s += "1" * t if s[now] == "2" else "2" * t
            now += t
            pre += 1
        return s[:n].count("1")