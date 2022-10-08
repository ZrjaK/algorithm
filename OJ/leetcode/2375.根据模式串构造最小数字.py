# 题目：2375.根据模式串构造最小数字
# 难度：MEDIUM
# 最后提交：2022-08-14 19:00:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestNumber(self, p: str) -> str:
        nums = [len(Ds) for Ds in p.split("I")]  # 把 D...DI  当成一个整块，其中D的个数可以为0
        l = 1
        res = ""
        for num in nums:
            r = l + num + 1          # [l, r) 为当前块的边界
            for x in range(l, r)[::-1]:      # 递减打印
                res += str(x)
            l = r
        return res