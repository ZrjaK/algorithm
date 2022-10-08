# 题目：667.优美的排列 II
# 难度：MEDIUM
# 最后提交：2022-09-08 10:06:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        return answer