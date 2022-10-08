for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print(0)
        continue
    k = n // 2
    r = 1
    for i in range(1,k+1):
        r *= i
    r *= r
    print(r % 998244353)