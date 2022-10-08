# 题目：剑指 Offer II 071.按权重生成随机数
# 难度：MEDIUM
# 最后提交：2022-10-08 13:08:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:

    def __init__(self, w: List[int]):
        self.h = list(accumulate(w))

    def pickIndex(self) -> int:
        x = random.randint(1, self.h[-1])
        return bisect_left(self.h, x)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()