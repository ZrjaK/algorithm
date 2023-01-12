# 题目：2283.判断一个数的数字计数是否等于数位的值
# 难度：EASY
# 最后提交：2023-01-11 00:20:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(v) for i, v in enumerate(num))