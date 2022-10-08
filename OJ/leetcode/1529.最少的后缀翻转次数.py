# 题目：1529.最少的后缀翻转次数
# 难度：MEDIUM
# 最后提交：2022-09-07 09:34:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFlips(self, target: str) -> int:
        res = len([i for i in target.split("0") if i])
        if not res:
            return 0
        res = 2 * res-1
        if  target[-1] == "0":
            res += 1
        return res