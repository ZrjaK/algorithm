# 题目：2555.两个线段获得的最多奖品
# 难度：MEDIUM
# 最后提交：2023-02-04 22:55:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1
 
    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])
 
    def __getitem__(self, idx):
        return self._data[0][idx]
    
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        ans = 0
        pos = {}
        h = []
        for i in sorted(set(prizePositions)):
            pos[i] = len(h)
            h.append(bisect_right(prizePositions, i + k) - bisect_left(prizePositions, i))
        rmq = RangeQuery(h, max)
        ans = 0
        for i in sorted(set(prizePositions)):
            s = h[pos[i]]
            t = bisect_right(prizePositions, i + k)
            if t < len(prizePositions):
                s += rmq.query(pos[prizePositions[t]], len(h))
            ans = max(ans, s)
        return ans
            