# 题目：1894.找到需要补充粉笔的学生编号
# 难度：MEDIUM
# 最后提交：2022-05-16 13:07:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k = k % s
        for i, v in enumerate(chalk):
            if k < v:
                return i
            k -= v