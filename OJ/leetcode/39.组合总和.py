# 题目：39.组合总和
# 难度：MEDIUM
# 最后提交：2022-04-11 10:40:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        @lru_cache(None)
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