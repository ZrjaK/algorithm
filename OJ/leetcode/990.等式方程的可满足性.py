# 题目：990.等式方程的可满足性
# 难度：MEDIUM
# 最后提交：2022-08-17 20:50:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for s in equations:
            if s[1] == "=":
                union(ord(s[0])-97, ord(s[3])-97)
        for s in equations:
            if s[1] == "!" and find(ord(s[0])-97) == find(ord(s[3])-97):
                return False
        return True

