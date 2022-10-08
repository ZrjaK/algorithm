# 题目：2283.判断一个数的数字计数是否等于数位的值
# 难度：EASY
# 最后提交：2022-05-28 22:38:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True