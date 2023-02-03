L, N = map(int, input().split())
N = 26**L - N
ans = []
for _ in range(L):
    ans.append(N % 26)
    N //= 26
ans = ans[::-1]
ans = [chr(i+97) for i in ans]
print("".join(ans))
