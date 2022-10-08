# 题目：762.二进制表示中质数个计算置位
# 难度：EASY
# 最后提交：2021-10-24 12:09:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        temp = {2, 3, 5, 7, 11, 13, 17, 19}
        return len([i for i in range(left, right + 1) if bin(i).count('1') in temp])