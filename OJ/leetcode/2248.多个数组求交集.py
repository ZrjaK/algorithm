# 题目：2248.多个数组求交集
# 难度：EASY
# 最后提交：2022-04-24 10:32:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i in range(1,1001):
            inn = True
            for j in nums:
                if i not in j:
                    inn = False
                    break
            if inn:
                res.append(i)
        return res