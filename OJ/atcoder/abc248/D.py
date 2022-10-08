from bisect import bisect_left, bisect_right


n = int(input())
a = [int(i) for i in input().split()]
d = [list() for _ in range(int(2*1e5+1))]
for i in range(n):
    d[a[i]].append(i)
# print(d)#[[], [1, 3], [], [0], [2], [4]
for _ in range(int(input())):
    l, r, x = [int(i) for i in input().split()]
    print(bisect_right(d[x], r-1)-bisect_left(d[x],l-1))