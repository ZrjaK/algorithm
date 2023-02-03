AAA, BBB = map(int, input().split())
A, B = AAA, BBB
n = int(input())
for _ in range(n):
    As, Ac, Bs, Bc = map(int, input().split())
    AA = (Ac == As + Bs)
    BB = (Bc == As + Bs)
    if AA and not BB:
        A -= 1
    if BB and not AA:
        B -= 1
    if A == -1:
        print("A")
        print(BBB-B)
        exit()
    if B == -1:
        print("B")
        print(AAA-A)
        exit()