# 题目：506.相对名次
# 难度：EASY
# 最后提交：2021-10-22 14:59:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        length = len(score)
        scoreSorted = sorted(score,reverse = True)
        dic = []
        for num in scoreSorted:
            dic.append(score.index(num))
        for i in range(length):
            if i == 0:
                score[dic[i]] = "Gold Medal"
            elif i == 1:
                score[dic[i]] = "Silver Medal"
            elif i == 2:
                score[dic[i]] = "Bronze Medal"
            else:
                score[dic[i]] = str(i+1)
        return score