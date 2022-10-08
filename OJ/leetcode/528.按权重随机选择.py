# 题目：528.按权重随机选择
# 难度：MEDIUM
# 最后提交：2022-05-01 19:53:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()