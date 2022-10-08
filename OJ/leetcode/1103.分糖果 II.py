# 题目：1103.分糖果 II
# 难度：EASY
# 最后提交：2021-11-06 16:10:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i%num_people] += i + 1
            candies -= i + 1
            i += 1
        res[(i-1)%num_people] += candies
        return res