for _ in range(int(input())):
    t = input().split()
    a, b = int(t[1]), int(t[2])
    if not (15 <= a <= b) or not (50 <= b <= 70):
        print(t[0])