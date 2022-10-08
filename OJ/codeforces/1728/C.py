for _ in range(int(input())):
    n = int(input())
    a = [-int(i) for i in input().split()]
    b = [-int(i) for i in input().split()]
    from heapq import heappush, heappop, heapify
    heapify(a)
    heapify(b)
    ans = 0
    while a:
        x, y = -heappop(a), -heappop(b)
        if x > y:
            x = len(str(x))
            heappush(a, -x)
            heappush(b, -y)
            ans += 1
        elif x < y:
            y = len(str(y))
            heappush(a, -x)
            heappush(b, -y)
            ans += 1
    print(ans)