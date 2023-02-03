input()
arr = list(map(int, input().split()))
print(len([i for i in arr if i % 2]), len([i for i in arr if i % 2 == 0]))