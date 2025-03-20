X = input()
n = int(input())
S = [input() for _ in range(n)]
S.sort(key=lambda x: [X.index(i) for i in x])
print(*S, sep="\n")