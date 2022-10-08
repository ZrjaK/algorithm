# 题目：135.分发糖果
# 难度：HARD
# 最后提交：2022-09-03 02:13:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                left[i] += left[i-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] += right[i+1]
        return sum([max(i, j) for i, j in zip(left, right)])
