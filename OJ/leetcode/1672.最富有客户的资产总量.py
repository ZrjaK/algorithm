# 题目：1672.最富有客户的资产总量
# 难度：EASY
# 最后提交：2022-04-14 17:04:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)