# 题目：1282.用户分组
# 难度：MEDIUM
# 最后提交：2022-05-01 14:31:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        res = []
        for i in d.keys():
            for j in range(0, len(d[i]), i):
                res.append(d[i][j:j+i])
        return res