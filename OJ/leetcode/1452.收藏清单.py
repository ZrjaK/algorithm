# 题目：1452.收藏清单
# 难度：MEDIUM
# 最后提交：2023-01-06 09:19:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def peopleIndexes(self, arr: List[List[str]]) -> List[int]:
        n = len(arr)
        for i in range(n):
            arr[i] = set(arr[i])
        ans = []
        for i in range(n):
            if all(len(arr[i] - (arr[i] & arr[j])) for j in range(n) if j != i):
                ans.append(i)
        return ans