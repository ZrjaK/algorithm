# 题目：2532.过桥的时间
# 难度：HARD
# 最后提交：2023-01-08 15:38:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        cur = 0
        workL, waitL, waitR, workR = [], [[-time[i][0] - time[i][2], -i, 0] for i in range(k)], [], []
        heapify(waitL)
        while n:
            while workL and workL[0][0] <= cur:
                p = heappop(workL)
                p[0], p[2] = p[2], p[0]
                heappush(waitL, p)  # 左边完成放箱
            while workR and workR[0][0] <= cur:
                p = heappop(workR)
                p[0], p[2] = p[2], p[0]
                heappush(waitR, p)  # 右边完成搬箱
            if waitR and waitR[0][2] <= cur:  # 右边过桥
                p = heappop(waitR)
                cur += time[-p[1]][2]
                p[2] = p[0]
                p[0] = cur + time[-p[1]][3]
                heappush(workL, p)  # 放箱
            elif waitL and waitL[0][2] <= cur:  # 左边过桥
                p = heappop(waitL)
                cur += time[-p[1]][0]
                p[2] = p[0]
                p[0] = cur + time[-p[1]][1]
                heappush(workR, p)  # 搬箱
                n -= 1
            elif len(workL) == 0:  # cur 过小，找个最小的放箱/搬箱完成时间来更新 cur
                cur = workR[0][0]
            elif len(workR) == 0:
                cur = workL[0][0]
            else:
                cur = min(workL[0][0], workR[0][0])
        while workR:
            t, i, _ = heappop(workR)  # 右边完成搬箱
            cur = max(t, cur) + time[-i][2]  # 过桥
        return cur  # 最后一个过桥的时间
