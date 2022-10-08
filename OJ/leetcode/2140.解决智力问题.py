# 题目：2140.解决智力问题
# 难度：MEDIUM
# 最后提交：2022-07-23 20:48:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def p(i):
            if i >= n:
                return 0
            return max(questions[i][0] + p(i+1+questions[i][1]), p(i+1))
        return p(0)