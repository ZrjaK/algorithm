# 题目：1952.三除数
# 难度：EASY
# 最后提交：2022-05-16 16:08:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isThree(self, n: int) -> bool:
        ans = 0
        for i in range(1,n+1):
            if n % i == 0:
                ans += 1
        return ans == 3