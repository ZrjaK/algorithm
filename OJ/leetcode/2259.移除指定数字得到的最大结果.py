# 题目：2259.移除指定数字得到的最大结果
# 难度：EASY
# 最后提交：2022-05-01 10:33:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        h = []
        for i in range(len(number)):
            if number[i] == digit:
                h.append(i)
        for i in h:
            res.append(int(number[:i]+number[i+1:]))
        return str(max(res))
        