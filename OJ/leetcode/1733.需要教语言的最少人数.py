# 题目：1733.需要教语言的最少人数
# 难度：MEDIUM
# 最后提交：2022-09-07 14:10:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        d = defaultdict(set)
        for i in range(len(languages)):
            for j in languages[i]:
                d[j].add(i+1)
        ans = 0
        v = set()
        for i, j in friendships:
            for k in range(1, n+1):
                if i in d[k] and j in d[k]:
                    break
            else:
                v.add(i)
                v.add(j)
        d = defaultdict(int)
        for i in range(len(languages)):
            if i+1 in v:
                for j in languages[i]:
                    d[j] += 1
        return len(v) - max([0]+list(d.values()))