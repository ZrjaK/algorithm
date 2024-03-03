from collections import deque
from heapq import heappush, heappop

q1 = deque()
q2 = []
q3 = []
q4 = []
ans1 = ans2 = ans3 = ans4 = 1
n = int(input())
c1 = c2 = 0
for _ in range(n):
    op, v = map(int, input().split())
    if op == 1:
        q1.append(v)
        q2.append(v)
        heappush(q3, -v)
        heappush(q4, v)
        c1 += 1
    if op == 2:
        if q1:ans1 &= v == q1.popleft()
        else:ans1 = 0
        if q2:ans2 &= v == q2.pop()
        else:ans2= 0
        if q3:ans3 &= v == -heappop(q3)
        else:ans3= 0
        if q4:ans4 &= v == heappop(q4)
        else:ans4 = 0
        c2 += 1
print(c1, c2)
ans = [ans1, ans2, ans3, ans4]
for i in ans:
    print("Yes" if i else "No")        