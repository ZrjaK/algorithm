# 题目：476.数字的补数
# 难度：EASY
# 最后提交：2021-10-22 12:49:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findComplement(self, num: int) -> int:
        num = list(str(bin(num))[2:])
        for i in range(len(num)):
            if num[i] == "0":
                num[i] = "1"
                continue
            if num[i] == "1":
                num[i] = "0"
        return int("".join(num), 2)