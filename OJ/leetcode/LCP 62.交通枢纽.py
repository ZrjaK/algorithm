# 题目：LCP 62.交通枢纽
# 难度：MEDIUM
# 最后提交：2022-09-24 15:14:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        v = set()
        d = defaultdict(list)
        c = defaultdict(list)
        for i, j in path:
            d[j].append(i)
            v.add(i)
            v.add(j)
            c[i].append(j)
        for j in d:
            if len(d[j]) == len(v)-1 and not c[j]:
                return j
        return -1