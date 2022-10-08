# 题目：2136.全部开花的最早一天
# 难度：HARD
# 最后提交：2022-09-15 22:54:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        c = 0
        ans = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda x:x[1], reverse=True):
            c += p
            ans = max(ans, c+g)
        return ans