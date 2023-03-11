# 题目：1247.交换字符使得字符串相同
# 难度：MEDIUM
# 最后提交：2023-02-25 00:12:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        xy = 0
        yx = 0
        for i, j in zip(s1, s2):
            if i == j:
                continue
            if i == "x":
                xy += 1
            else:
                yx += 1
        ans = yx // 2 + xy // 2
        yx %= 2
        xy %= 2
        if yx == xy == 1:
            return ans + 2
        elif yx == xy == 0:
            return ans
        return -1