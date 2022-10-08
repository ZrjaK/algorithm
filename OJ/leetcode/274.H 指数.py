# 题目：274.H 指数
# 难度：MEDIUM
# 最后提交：2022-08-27 15:07:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations), -1, -1):
            if all(j>=i for j in citations[:i]) and all(j<=i for j in citations[i+1:]):
                return i