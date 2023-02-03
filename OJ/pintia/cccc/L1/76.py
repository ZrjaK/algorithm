n, m = map(int, input().split())
for _ in range(n):
    t = float(input())
    if t < m:
        print("On Sale!", t)