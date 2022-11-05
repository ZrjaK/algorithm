# 题目：754.到达终点数字
# 难度：MEDIUM
# 最后提交：2022-11-04 22:04:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = s = 0
        while s < target:
            k += 1
            s += k
        if (s-target) % 2 == 0:
            return k
        else:
            if k % 2 == 0:
                return k+1
            else:
                return k+2