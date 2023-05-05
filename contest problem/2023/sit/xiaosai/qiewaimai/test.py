for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if arr[:j-i+1] == arr[i:j+1]:
                ans += 1
    print(ans)