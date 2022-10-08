# 题目：2383.赢得比赛需要的最少训练时长
# 难度：EASY
# 最后提交：2022-08-21 10:35:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for i, j in zip(energy, experience):
            if initialEnergy <= i:
                ans += i-initialEnergy+1
                initialEnergy = i+1
            initialEnergy -= i
            if initialExperience <= j:
                ans += j - initialExperience + 1
                initialExperience = j+1
            initialExperience += j
        return ans