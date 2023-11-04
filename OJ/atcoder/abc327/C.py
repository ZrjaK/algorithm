a = [[int(i) for i in input().split()] for _ in range(9)]
for i in range(9):
    if len(set(a[i])) != 9:
        exit(print("No"))
for j in range(9):
    if len(set([a[i][j] for i in range(9)])) != 9:
        exit(print("No"))
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        v = set()
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                v.add(a[x][y])
        if len(v) != 9:
            exit(print("No"))
print("Yes")