# 题目：2180.统计各位数字之和为偶数的整数个数
# 难度：EASY
# 最后提交：2023-01-06 00:43:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countEven(self, num: int) -> int:
        return len([i for i in range(2, num+1) if sum(int(j) for j in str(i)) % 2 == 0])