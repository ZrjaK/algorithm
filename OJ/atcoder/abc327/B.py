B = int(input())
for i in range(1, 60):
    if i**i == B:
        exit(print(i))
print(-1)