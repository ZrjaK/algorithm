for _ in range(int(input())):
    s = input().split()
    a, b = int(s[0]), int(s[1])
    if a == 0:
        print(1)
        continue
    print(a+b*2+1)

        
    