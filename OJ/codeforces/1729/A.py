for _ in range(int(input())):
    a, b, c = [int(i) for i in input().split()]
    if a-1 > abs(b-c) + c-1:
        print(2)
    elif a-1 < abs(b-c) + c-1:
        print(1)
    else:
        print(3)