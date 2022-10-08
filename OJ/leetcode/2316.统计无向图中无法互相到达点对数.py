# 题目：2316.统计无向图中无法互相到达点对数
# 难度：MEDIUM
# 最后提交：2022-06-25 23:15:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.co = 0  # 用于记录群的个数
                self.parent = []  # 索引是每个节点本身，值是每个节点的父节点
                self.size = []  # 用于记录每个群的节点数目

            #
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]  # 用于路径压缩
                    x = self.parent[x]
                return x

            def union(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)
                if rootP == rootQ:
                    return
                # 下面的这个if语句用将节点数少的合并到节点数多的群中
                if self.size[rootP] > self.size[rootQ]:
                    self.parent[rootQ] = rootP
                    self.size[rootP] += self.size[rootQ]
                else:
                    self.parent[rootP] = rootQ
                    self.size[rootQ] += self.size[rootP]
                self.co -= 1

            # 用于判断p和q之间是否连通，如果两个节点的父节点是相同的，那么就是连通的
            def connected(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)
                return rootP == rootQ

            # 返回有多少个群
            def count(self):
                return self.co

            # 初始化，节点的父节点就是其本身，假设n=10，那么就有10个群，self.parent=[0,1,2,3,4,5,6,7,8,9]，self.parent[0]=0表示0节点的父节点是0。每个群的size，也就是包含的节点数目就是1，self.size[0]=1。
            def uf(self, n):
                self.co = n
                self.parent = [0 for _ in range(n)]
                self.size = [0 for _ in range(n)]
                for i in range(n):
                    self.parent[i] = i
                    self.size[i] = 1
        unionF = UnionFind()
        unionF.uf(n)
        for i, j in edges:
            unionF.union(i, j)
        for i in range(n):
            unionF.find(i)
        for i in range(n):
            unionF.find(i)
        # print(unionF.parent)
        # print(unionF.size)
        ans = n*(n-1)//2
        t = 0
        for i in set(unionF.parent):
            t += unionF.size[i]*(unionF.size[i]-1)//2
        return ans-t