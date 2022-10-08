# 题目：845.数组中的最长山脉
# 难度：MEDIUM
# 最后提交：2022-05-05 10:13:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        h = [0] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                h[i] = h[i-1] + 1
        j = [0] * n
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                j[i] = j[i+1] + 1
        ans = 0
        # print(h, j)
        for a, b in zip(h, j):
            if a > 0 and b > 0:
                ans = max(ans, a+b)
        return ans+1 if ans else 0