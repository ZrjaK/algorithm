# 题目：剑指 Offer II 081.允许重复选择元素的组合
# 难度：MEDIUM
# 最后提交：2022-10-08 14:55:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def p(index, tar, ha):
            if tar == 0:
                res.append(list(ha))
                return
            if index == len(candidates):
                return
            for i in range(tar//candidates[index]+1):
                p(index+1, tar-i*candidates[index], tuple(list(ha)+[candidates[index]]*i))
        p(0, target, tuple())
        return res