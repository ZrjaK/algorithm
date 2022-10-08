# 题目：1557.可以到达所有点的最少点数目
# 难度：MEDIUM
# 最后提交：2022-05-07 16:59:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list({i for i,_ in edges} - {j for _, j in edges})