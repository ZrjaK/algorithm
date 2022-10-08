# 题目：1439.有序矩阵中的第 k 个最小数组和
# 难度：HARD
# 最后提交：2022-09-21 09:40:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList
        m, n = len(mat), len(mat[0])
        s = SortedList(mat[0])
        for i in range(1, m):
            cur = SortedList()
            for num in mat[i]:
                for p in s:
                    cur.add(num + p)
                    if len(cur) > k and num + p > cur[k - 1]:
                        break
            s = cur[:k]
        return s[k - 1]