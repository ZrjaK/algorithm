# 题目：2545.根据第 K 场考试的分数排序
# 难度：MEDIUM
# 最后提交：2023-01-22 14:08:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: -x[k])
        return score