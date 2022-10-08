# 题目：1354.多次求和构造目标数组
# 难度：HARD
# 最后提交：2022-09-15 11:08:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        s = sum(target)
        pq = [-i for i in target]
        heapify(pq)
        while -pq[0] != 1:
            t = -heappop(pq)
            s -= t
            if t == -pq[0]:
                return False
            k = ceil((t+pq[0]) / s)
            t -= s * k
            s += t
            if t < 1:
                return False
            heappush(pq, -t)
        return True