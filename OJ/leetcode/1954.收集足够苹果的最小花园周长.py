# 题目：1954.收集足够苹果的最小花园周长
# 难度：MEDIUM
# 最后提交：2022-05-16 16:44:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i = s = 0
        while s < neededApples:
            i += 1
            s += 12*i**2
        return i*8