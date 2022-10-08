# 题目：2149.按符号重排数组
# 难度：MEDIUM
# 最后提交：2022-06-21 13:03:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [i for i in nums if i < 0][::-1]
        b = [i for i in nums if i > 0][::-1]
        res = []
        while a:
            res.append(b.pop())
            res.append(a.pop())
        return res