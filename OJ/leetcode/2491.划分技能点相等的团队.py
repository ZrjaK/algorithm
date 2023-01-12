# 题目：2491.划分技能点相等的团队
# 难度：MEDIUM
# 最后提交：2022-12-04 18:59:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        s = sum(skill)
        if s % (n // 2):
            return -1
        t = s // (n // 2)
        ans = 0
        for i in range(n//2):
            if skill[i] + skill[~i] != t:
                return -1
            ans += skill[i] * skill[~i]
        return ans
        