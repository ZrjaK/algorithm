# 题目：869.重新排序得到 2 的幂
# 难度：MEDIUM
# 最后提交：2022-03-26 08:41:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = set()
        k = 1
        while k <= 10**9:
            s.add("".join(sorted(list(str(k)))))
            k *= 2
        return "".join(sorted(list(str(n)))) in s