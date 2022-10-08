for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(nums.index(max(nums))+1)