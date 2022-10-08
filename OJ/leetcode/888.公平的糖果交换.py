# 题目：888.公平的糖果交换
# 难度：EASY
# 最后提交：2021-11-01 22:14:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        for i in aliceSizes:
            x = (b-a)//2+i
            if x in bobSizes:
                return[i,x]
