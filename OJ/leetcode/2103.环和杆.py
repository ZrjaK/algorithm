# 题目：2103.环和杆
# 难度：EASY
# 最后提交：2022-10-03 14:46:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        for i, j in zip(rings[::2], rings[1::2]):
            d[j].add(i)
        return len([1 for i in d.values() if len(i) == 3])