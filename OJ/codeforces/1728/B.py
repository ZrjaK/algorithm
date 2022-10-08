for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(" ".join([str(i) for i in list(range(n-2, 0, -1)) + [n-1, n]]))
    else:
        print(" ".join([str(i) for i in list(range(n-2, 3, -1)) + [1,2,3,n-1,n]]))