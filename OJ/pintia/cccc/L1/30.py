from collections import deque

n = int(input())
q1 = deque()
q0 = deque()
for i in range(n):
    t = input().split()
    if t[0] == "0":
        q0.append((t[1], i))
    else:
        q1.append((t[1], i))
for _ in range(n//2):
    if q0[0][1] < q1[0][1]:
        print(q0.popleft()[0], q1.pop()[0])
    else:
        print(q1.popleft()[0], q0.pop()[0])