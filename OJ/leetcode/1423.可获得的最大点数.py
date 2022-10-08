# 题目：1423.可获得的最大点数
# 难度：MEDIUM
# 最后提交：2022-05-23 11:09:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        ans = s
        for i in range(1,k+1):
            s -= cardPoints[k-i]
            s += cardPoints[-i]
            ans = max(ans, s)
        return ans