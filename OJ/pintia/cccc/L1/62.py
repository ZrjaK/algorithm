for _ in range(int(input())):
    s = input()
    if sum(int(i) for i in s[:3]) == sum(int(i) for i in s[-3:]):
        print("You are lucky!")
    else:
        print("Wish you good luck.")