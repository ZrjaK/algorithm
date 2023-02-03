arr = [int(i) for i in input().split()]
while 1:
    t = int(input())
    if not 0 <= t < 24:
        break
    if arr[t] > 50:
        print(arr[t], "Yes") 
    else:
        print(arr[t], "No")