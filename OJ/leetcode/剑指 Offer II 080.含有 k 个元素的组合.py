# 题目：剑指 Offer II 080.含有 k 个元素的组合
# 难度：MEDIUM
# 最后提交：2022-10-08 14:52:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        for mask in range(1<<n):
            if mask.bit_count() != k:
                continue
            t = []
            for i in range(n):
                if mask>>i & 1:
                    t.append(i+1)
            res.append(t)
        return res