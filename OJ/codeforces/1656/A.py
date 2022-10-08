for _ in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    print(l.index(min(l))+1, l.index(max(l))+1)