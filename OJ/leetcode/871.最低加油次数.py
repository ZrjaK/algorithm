# 题目：871.最低加油次数
# 难度：HARD
# 最后提交：2022-03-26 09:15:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        curStation = 0
        curFuel = startFuel
        s = SortedList()
        count = 0
        stations.append([target, 0])
        for nextStation, j in stations:
            while curFuel < nextStation - curStation:
                if len(s) == 0:
                    return -1
                curFuel += s.pop()
                count += 1
            s.add(j)
            if curFuel + curStation > target:
                break
        return count

                
            