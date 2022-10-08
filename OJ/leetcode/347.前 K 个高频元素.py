# 题目：347.前 K 个高频元素
# 难度：MEDIUM
# 最后提交：2022-08-27 15:29:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        pq = []
        for i in d.keys():
            heappush(pq, (d[i], i))
            if len(pq) > k:
                heappop(pq)
        return [i[1] for i in pq]