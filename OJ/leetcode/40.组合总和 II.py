# 题目：40.组合总和 II
# 难度：MEDIUM
# 最后提交：2022-04-11 10:49:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        @lru_cache(None)
        def p(index, tar, ha):
            if tar < 0:
                return
            if tar == 0:
                res.add(tuple(sorted(list(ha))))
                return
            if index == len(candidates):
                return
            p(index+1, tar, ha)
            p(index+1, tar-candidates[index], tuple(list(ha)+[candidates[index]]))
        p(0, target, tuple())
        return [list(i) for i in res]