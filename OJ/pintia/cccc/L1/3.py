from collections import Counter
c = Counter(input())
for i in sorted(c):
    print(f"{i}:{c[i]}")