# 题目：216.组合总和 III
# 难度：MEDIUM
# 最后提交：2022-04-11 11:07:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        @lru_cache(None)
        def p(cur, krest, nrest, ha):
            if nrest == krest == 0:
                res.add(tuple(sorted(list(ha))))
            if nrest < 0 or cur == 10 or krest < 0:
                return
            p(cur+1, krest-1, nrest-cur, tuple(list(ha)+[cur]))
            p(cur+1, krest, nrest, ha)
        p(1, k, n, tuple())
        return list(res)