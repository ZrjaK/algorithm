# 题目：978.最长湍流子数组
# 难度：MEDIUM
# 最后提交：2022-05-21 22:25:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l = r = 0
        ans = 1
        while r + 1 < n:
            if l == r:
                if arr[l] == arr[l+1]:
                    l += 1
                r += 1
            else:
                if arr[r-1] < arr[r] > arr[r+1] or arr[r-1] > arr[r] < arr[r+1]:
                    r += 1
                else:
                    l = r
            ans = max(ans, r-l+1)
        return ans