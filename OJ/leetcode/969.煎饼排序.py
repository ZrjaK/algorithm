# 题目：969.煎饼排序
# 难度：MEDIUM
# 最后提交：2022-06-08 04:09:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        n = len(arr)
        res = []
        c = n
        while sorted(arr) != arr:
            t = arr.index(max(arr[:c]))
            if t >= len(arr) // 2:
                reverse(0, c-1)
                res.append(c)

            t = arr.index(max(arr[:c]))
            reverse(0, t)
            res.append(t+1)

            reverse(0, c-1)
            res.append(c)
            c -= 1
        return res