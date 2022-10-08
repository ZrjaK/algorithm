# 题目：1743.从相邻元素对还原数组
# 难度：MEDIUM
# 最后提交：2022-10-03 16:42:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, j in adjacentPairs:
            d[i].append(j)
            d[j].append(i)
        v = set()
        res = []
        for i in sorted(d, key=lambda x: len(d[x])):
            q = deque([i])
            while q:
                t = q.popleft()
                if t in v:
                    continue
                v.add(t)
                res.append(t)
                for j in d[t]:
                    q.append(j)
            break
        return res