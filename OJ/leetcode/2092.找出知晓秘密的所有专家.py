# 题目：2092.找出知晓秘密的所有专家
# 难度：HARD
# 最后提交：2022-09-14 16:03:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2], reverse=True)
        h = []
        while meetings:
            t = []
            f = meetings.pop()
            t.append(f[:2])
            while meetings and meetings[-1][2] == f[2]:
                f = meetings.pop()
                t.append(f[:2])
            h.append(t)
        parent = list(range(n))
        parent[firstPerson] = 0
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        def seperate(i, j):
            parent[i] = i
            parent[j] = j
        for e in h:
            for i, j in e:
                if find(i) == 0:
                    i, j = j, i
                union(i, j)
            for i, j in e:
                if find(i) != 0:
                    seperate(i, j)
        print(parent)
        return [i for i in range(n) if find(i) == 0]