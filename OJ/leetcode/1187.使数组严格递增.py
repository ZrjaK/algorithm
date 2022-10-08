# 题目：1187.使数组严格递增
# 难度：HARD
# 最后提交：2022-09-28 14:17:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        arr1 += [-1]
        arr2.sort()
        @cache
        def p(i, j, change):
            if i == n:
                return 0
            if change:
                pre = arr2[j]
            else:
                pre = arr1[j]
            res = 1e99
            if arr1[i] > pre:
                res = min(res, p(i+1, i, False))
            t = bisect_right(arr2, pre)
            if t == m:
                if arr1[i] <= pre:
                    return 1e99
            else:
                res = min(res, 1 + p(i+1, t, True))
            return res
        res = p(0, -1, False)
        return res if res < 1e90 else -1