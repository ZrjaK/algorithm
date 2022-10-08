# 题目：1483.树节点的第 K 个祖先
# 难度：HARD
# 最后提交：2022-09-19 15:57:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        dp = [[-1] * 32 for _ in range(n)]
        for i in range(n):
            dp[i][0] = parent[i]
        for j in range(1, 32):
            for i in range(n):
                if dp[i][j-1] != -1:
                    dp[i][j] = dp[dp[i][j-1]][j-1]
        self.dp = dp


    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0 or node == -1:
            return node
        f = k & -k
        t = -1
        while f:
            t += 1
            f >>= 1
        if self.dp[node][t] == -1:
            return -1
        return self.getKthAncestor(self.dp[node][t], k&k-1)

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)