for _ in range(int(input())):
    s = input().split()
    n, B, x, y = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    arr = [0] * (n+1)
    for i in range(1, n+1):
        if arr[i-1] + x <= B:
            arr[i] = arr[i-1] + x
        else:
            arr[i] = arr[i-1] - y
    print(sum(arr))