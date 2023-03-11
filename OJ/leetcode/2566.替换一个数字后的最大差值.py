# 题目：2566.替换一个数字后的最大差值
# 难度：EASY
# 最后提交：2023-02-18 22:33:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMaxDifference(self, num: int) -> int:
        ma = mi = num
        for i in range(10):
            for j in range(10):
                s = str(num)
                s = s.replace(str(i), str(j))
                ma = max(ma, int(s))
                mi = min(mi, int(s))
        return ma - mi