# 题目：2404.出现最频繁的偶数元素
# 难度：EASY
# 最后提交：2022-09-11 10:31:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        h = []
        for i in nums:
            if i % 2 == 0:
                h.append(i)
        c = Counter(h)
        if not c.values():
            return -1
        ans = -1
        t = 0
        for i in sorted(c, reverse=True):
            if c[i] >= t:
                ans = i
                t = c[i]
        return ans