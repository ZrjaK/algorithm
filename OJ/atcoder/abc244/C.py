s = set([])
n = int(input())
while len(s) < 2 * n + 1:
    for i in range(1, 2*n+2):
        if i not in s:
            s.add(i)
            print(i)
            break
    s.add(int(input()))