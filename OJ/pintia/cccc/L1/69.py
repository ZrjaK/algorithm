a, b, c, d, e, f = map(int, input().split())
t = max(a, b, c, d)
if t - min(a, b, c, d) <= f and min(a, b, c, d) >= e:
    exit(print("Normal"))
ans = []
for i in [a, b, c, d]:
    if t - i > f or i < e:
        ans.append(i)
if len(ans) == 1:
    print(f"Warning: please check #{[a, b, c, d].index(ans[0]) + 1}!")
else:
    print("Warning: please check all the tires!")