a, b = map(int, input().split())
h = list(range(a, b+1))
ans = 0
for i in range(len(h)):
    print("%5d" % h[i], end = '')
    ans += h[i]
    if i % 5 == 4:
        print()
if (b - a + 1) % 5 != 0:
    print()
print("Sum =", ans)
