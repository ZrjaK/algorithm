# 题目：2300.咒语和药水的成功对数
# 难度：MEDIUM
# 最后提交：2022-06-11 22:45:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in spells:
            t = bisect_left(potions, success/i)
            res.append(len(potions)-t)
        return res