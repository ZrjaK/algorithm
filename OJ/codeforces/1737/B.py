for _ in range(int(input())):
    l, r = [int(i) for i in input().split()]
    def calc(n):
        ans = 0
        for x in range(3):
            l, r = 0, 2*10**9
            while l <= r:
                mid = l+r>>1
                if mid * (mid + x) > n:
                    r = mid - 1
                else:
                    l = mid + 1
            ans += l
        return ans
    print(calc(r)-calc(l-1))