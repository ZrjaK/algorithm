# 题目：1847.最近的房间
# 难度：HARD
# 最后提交：2022-09-18 20:09:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        queries = [[x, y, i] for i, (x, y) in enumerate(queries)]
        queries.sort(key=lambda x: x[1])
        rooms.sort(key=lambda x: x[1])
        ans = [-1] * len(queries)
        h = []
        while queries:
            p, s, i = queries.pop()
            while rooms and rooms[-1][1] >= s:
                insort(h, rooms.pop()[0])
            if not h:
                continue
            t = bisect_left(h, p)
            if t == len(h) or (t > 0 and abs(p-h[t-1]) <= abs(p-h[t])):
                ans[i] = h[t-1]
            else:
                ans[i] = h[t]
        return ans