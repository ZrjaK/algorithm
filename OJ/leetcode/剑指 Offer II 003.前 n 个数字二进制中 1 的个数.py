# 题目：剑指 Offer II 003.前 n 个数字二进制中 1 的个数
# 难度：EASY
# 最后提交：2022-10-04 00:47:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            ans[i] = ans[i>>1] + (i & 1)
        return ans