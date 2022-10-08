# 题目：1562.查找大小为 M 的最新分组
# 难度：MEDIUM
# 最后提交：2022-05-07 23:44:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        s = SortedList()
        s.add(0)
        s.add(n+1)
        for i in range(n-1, -1, -1):
            t = s.bisect_left(arr[i])-1
            if arr[i] - s[t] - 1 == m or s[t+1] - arr[i] - 1 == m:
                return i
            else:
                s.add(arr[i])
        return -1