# 题目：2508.添加边使所有节点度数都为偶数
# 难度：HARD
# 最后提交：2022-12-18 16:26:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degree = [0] * n
        d = defaultdict(set)
        for i, j in edges:
            i -= 1
            j -= 1
            degree[i] += 1
            degree[j] -= 1
            d[i].add(j)
            d[j].add(i)
        h = [i for i in range(n) if degree[i] % 2]
        if len(h) % 2 or len(h) > 4:
            return False
        if not h:
            return True
        def check(x, y):
            if x not in d[y]:
                return True
            for i in range(n):
                if i not in h and x not in d[i] and y not in d[i]:
                    return True
            return False
        if len(h) == 2:
            return check(h[0], h[1])
        else:
            res = False
            res |= check(h[0], h[1]) and check(h[2], h[3])
            res |= check(h[0], h[2]) and check(h[1], h[3])
            res |= check(h[0], h[3]) and check(h[1], h[2])
            return res