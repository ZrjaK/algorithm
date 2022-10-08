# 题目：1579.保证图可完全遍历
# 难度：HARD
# 最后提交：2022-09-20 23:39:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parentA = list(range(n+1))
        parentB = list(range(n+1))
        def findA(i):
            if parentA[i] != i:
                parentA[i] = findA(parentA[i])
            return parentA[i]
        def findB(i):
            if parentB[i] != i:
                parentB[i] = findB(parentB[i])
            return parentB[i]
        def unionA(i, j):
            parentA[findA(i)] = parentA[findA(j)]
        def unionB(i, j):
            parentB[findB(i)] = parentB[findB(j)]
        edges.sort(key=lambda x:x[0], reverse=True)
        setA = set()
        setB = set()
        for idx, (t, i, j) in enumerate(edges):
            if t == 3 or t == 1:
                if findA(i) == findA(j):
                    setA.add(idx)
                unionA(i, j)
            if t == 3 or t == 2:
                if findB(i) == findB(j):
                    setB.add(idx)
                unionB(i, j)
        if any(findA(parentA[i]) != findA(parentA[1]) for i in range(1, n+1)) or \
            any(findB(parentB[i]) != findB(parentB[1]) for i in range(1, n+1)):
            return -1
        return len(setA|setB)