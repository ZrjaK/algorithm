# 题目：986.区间列表的交集
# 难度：MEDIUM
# 最后提交：2022-06-08 04:25:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            starti, endi = firstList[i][0], firstList[i][1]
            startj, endj = secondList[j][0], secondList[j][1]
            if endi < startj:
                i += 1
                continue
            if starti > endj:
                j += 1
                continue
            if starti < startj:
                if endi < endj:
                    res.append([startj, endi])
                    i += 1
                elif endi > endj:
                    res.append([startj, endj])
                    j += 1
                else:
                    res.append([startj, endj])
                    i += 1
                    j += 1
            elif startj < starti:
                if endj < endi:
                    res.append([starti, endj])
                    j +=  1
                elif endj > endi:
                    res.append([starti, endi])
                    i += 1
                else:
                    res.append([starti, endi])
                    i += 1
                    j += 1
            else:
                if endj < endi:
                    res.append([starti, endj])
                    j +=  1
                elif endj > endi:
                    res.append([startj, endi])
                    i += 1
                else:
                    res.append([starti, endi])
                    i += 1
                    j += 1
        return res