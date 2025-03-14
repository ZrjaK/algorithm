S = input()
L = []
for _ in range(len(S)):
    S = S[1:] + S[:1]
    L.append(S)
L.sort()
print(min(L))
print(max(L))