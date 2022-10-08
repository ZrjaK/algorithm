q = []
for i in range(int(input())):
    t = input().split()
    if len(t) == 3:
        _, x, c = [int(j) for j in t]
        q.append([x,c])
    else:
        s = 0
        _, c = [int(j) for j in t]
        while c > q[0][1]:
            s += q[0][1]*q[0][0]
            c -= q[0][1]
            q.pop(0)
        if c < q[0][1]:
            s += c*q[0][0]
            q[0][1] -= c
        elif c == q[0][1]:
            s += c*q[0][0]
            q.pop(0)
        print(s)