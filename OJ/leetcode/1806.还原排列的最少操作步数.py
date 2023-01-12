# 题目：1806.还原排列的最少操作步数
# 难度：MEDIUM
# 最后提交：2023-01-09 03:43:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = list(range(n))
        t = deepcopy(arr)
        for i in range(1, n+1):
            arr = [[arr[i//2], arr[n//2+(i-1)//2]][i%2] for i in range(n)]
            if arr == t:
                return i