input()
arr = [int(i) for i in input().split()]
print(min(arr), arr.count(min(arr)))
print(max(arr), arr.count(max(arr)))