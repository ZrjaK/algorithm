for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    s = input()
    from collections import Counter
    c = Counter()
    for i in s:
        c[ord(i)-97] += 1
    ans = ""
    for _ in range(k):
        for i in range(n//k, -1, -1):
            if all(c[j] > 0 for j in range(i)):
                ans += chr(i+97)
                for j in range(i):
                    c[j] -= 1
                break
    print(ans)