# 题目：1899.合并若干三元组以形成目标三元组
# 难度：MEDIUM
# 最后提交：2022-09-08 11:38:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(3):
            triplets.sort(key=lambda x:x[i])
            while triplets and triplets[-1][i] > target[i]:
                triplets.pop()
        res = [0] * 3
        for t in triplets:
            for i in range(3):
                res[i] = max(res[i], t[i])
        return res == target