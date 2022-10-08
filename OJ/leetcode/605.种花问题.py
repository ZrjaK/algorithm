# 题目：605.种花问题
# 难度：EASY
# 最后提交：2021-10-23 10:41:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp = [0]+flowerbed+[0]
        for i in range(1, len(tmp)-1):
            if tmp[i-1] == 0 and tmp[i] == 0 and tmp[i+1] == 0:
                tmp[i] = 1  # 在 i 处栽上花
                n -= 1   
        return n <= 0   # n 小于等于 0 ，表示可以栽完花