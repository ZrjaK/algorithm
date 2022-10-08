# 题目：2332.坐上公交的最晚时间
# 难度：MEDIUM
# 最后提交：2022-07-10 11:49:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                c -= 1
                j += 1
        j -= 1
        ans = buses[-1] if c else passengers[j]
        while j >= 0 and passengers[j] == ans:  # 往前找没人到达的时刻
            ans -= 1
            j -= 1
        return ans