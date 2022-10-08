# 题目：7.整数反转
# 难度：MEDIUM
# 最后提交：2021-10-20 13:06:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int("-" + str(abs(x))[::-1])
            if x < - 2**31:
                return 0
            return x    
        x = int(str(x)[::-1])
        if x > 2**31 -1:
            return 0
        return x