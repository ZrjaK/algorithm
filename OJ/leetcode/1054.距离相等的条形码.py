# 题目：1054.距离相等的条形码
# 难度：MEDIUM
# 最后提交：2022-08-30 02:17:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        pq = []
        for i, j in c.items():
            heappush(pq, [-j, i])
        res = []
        while len(pq) > 1:
            t1 = heappop(pq)
            t2 = heappop(pq)
            t1[0] += 1
            t2[0] += 1
            res.append(t1[1])
            res.append(t2[1])
            if t1[0]:
                heappush(pq, t1)
            if t2[0]:
                heappush(pq, t2)
        if pq:
            res.append(heappop(pq)[1])
        return res