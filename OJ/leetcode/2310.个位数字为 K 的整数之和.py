# 题目：2310.个位数字为 K 的整数之和
# 难度：MEDIUM
# 最后提交：2022-06-19 10:42:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, num+1):
            t = num - i * k
            if t % 10 == 0:
                if t >= 0:
                    return i
        return -1