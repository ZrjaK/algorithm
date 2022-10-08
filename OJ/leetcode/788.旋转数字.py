# 题目：788.旋转数字
# 难度：MEDIUM
# 最后提交：2022-09-25 10:25:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            s = str(i)
            if any(str(j) in s for j in [2,5,6,9]):
                if not any(str(j) in s for j in [3,4,7]):
                    ans += 1
        return ans