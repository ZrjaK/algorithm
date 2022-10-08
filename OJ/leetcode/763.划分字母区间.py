# 题目：763.划分字母区间
# 难度：MEDIUM
# 最后提交：2022-06-03 15:33:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        h = defaultdict(int)
        for i, a in enumerate(s):
            h[a] = i
        p1 = p2 = right = 0
        res = []
        c = 0
        while p1 < n and p2 < n:
            c = h[s[p1]]
            # print(p1, p2)
            while p2 < c:
                c = max(c, h[s[p2]])
                p2 += 1
            res.append(p2-p1+1)
            p1 = p2 + 1
        return res