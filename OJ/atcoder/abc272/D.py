n, m = [int(i) for i in input().split()]
ans = [[1e99] * n for _ in range(n)]
ans[0][0] = 0
h = []
for i in range(int(m**0.5)+1):
    t = (m-i**2)**0.5
    if int(t) == t:
        h.append([i, int(t)])
        h.append([-i, int(t)])
        h.append([i, -int(t)])
        h.append([-i, -int(t)])
from heapq import heappop, heappush
pq = [[0, 0, 0]]
while pq:
    s, x, y = heappop(pq)
    for dx, dy in h:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and (s + 1 < ans[nx][ny] or s + 1 < ans[ny][nx]):
            ans[nx][ny] = s + 1
            ans[ny][nx] = s + 1
            heappush(pq, [s+1, nx, ny])
            heappush(pq, [s+1, ny, nx])
for i in ans:
    for j in i:
        if j == 1e99:
            print(-1, end=" ")
        else:
            print(j, end=" ")
    print()