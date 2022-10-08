# 题目：134.加油站
# 难度：MEDIUM
# 最后提交：2022-09-05 10:33:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sg = sc = c = 0
            while c < n:
                sg += gas[(i + c) % n]
                sc += cost[(i + c) % n]
                if sc > sg:
                    break
                c += 1
            if c == n:
                return i
            else:
                i += c + 1
        return -1