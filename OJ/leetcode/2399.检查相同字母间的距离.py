# 题目：2399.检查相同字母间的距离
# 难度：EASY
# 最后提交：2022-09-04 10:32:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        d = defaultdict(list)
        for i in range(n):
            d[ord(s[i])-97].append(i)
        for i in range(26):
            if d[i] and d[i][1]-d[i][0]-1 != distance[i]:
                return False
        return True