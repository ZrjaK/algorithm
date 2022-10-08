# 题目：841.钥匙和房间
# 难度：MEDIUM
# 最后提交：2022-08-01 18:25:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set()
        while q:
            t = q.popleft()
            if t in visited:
                continue
            visited.add(t)
            for nxt in rooms[t]:
                q.append(nxt)
        return len(visited) == len(rooms)