# 题目：372.超级次方
# 难度：MEDIUM
# 最后提交：2022-09-13 09:43:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join(str(i) for i in b)), 1337)