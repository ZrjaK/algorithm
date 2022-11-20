# 题目：1710.卡车上的最大单元数
# 难度：EASY
# 最后提交：2022-11-15 09:49:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for i, j in boxTypes:
            if i <= truckSize:
                ans += i * j
                truckSize -= i
            else:
                ans += j * truckSize
                break
        return ans