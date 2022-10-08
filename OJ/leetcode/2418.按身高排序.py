# 题目：2418.按身高排序
# 难度：EASY
# 最后提交：2022-09-25 10:31:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = list(zip(names, heights))
        h.sort(key=lambda x:-x[1])
        return [i[0] for i in h]