# 题目：1477.找两个和为目标值且不重叠的子数组
# 难度：MEDIUM
# 最后提交：2022-07-23 22:06:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        h = list(accumulate(arr))
        l = [1e99] * n
        for i in range(n):
            if i == 0:
                if h[i] == target:
                    l[i] = 1
                continue
            t = bisect_left(h, h[i]-target)
            if t == 0 and h[i] == target:
                l[i] = i+1
            if h[t] + target == h[i]:
                l[i] = i-t
        h2 = list(accumulate(arr[::-1]))
        r = [1e99] * n
        for i in range(n):
            if i == 0:
                if h2[i] == target:
                    r[i] = 1
                continue
            t = bisect_left(h2, h2[i]-target)
            if t == 0 and h2[i] == target:
                r[i] = i+1
            if h2[t] + target == h2[i]:
                r[i] = i-t
        r = r[::-1]
        r2 = [0] * n + [1e99]
        for i in range(n-1, -1, -1):
            r2[i] = min(r[i], r2[i+1])
        ans = 1e99
        for i in range(n-1):
            ans = min(ans, l[i] + r2[i+1])
        return ans if ans < 1e90 else -1