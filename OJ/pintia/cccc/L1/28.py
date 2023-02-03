def check(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")