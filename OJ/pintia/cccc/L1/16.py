M = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
h = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

f = 1
n = int(input())
for _ in range(n):
    s = input()
    t = 0
    try:
        for i in range(17):
            t += int(s[i]) * h[i]
    except:
        f = 0
        print(s)
        continue
    if str(M[t % 11]) != s[-1]:
        print(s)
        f = 0
if f:
    print("All passed")