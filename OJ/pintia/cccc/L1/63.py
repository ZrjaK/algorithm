for _ in range(int(input())):
    g, h, w = map(int, input().split())
    ans = []
    if g:
        H = 130
        W = 27
    else:
        H = 129
        W = 25
    if h > H:
        ans.append("ni li hai!")
    elif h < H:
        ans.append("duo chi yu!")
    else:
        ans.append("wan mei!")
    if w > W:
        ans.append("shao chi rou!")
    elif w < W:
        ans.append("duo chi rou!")
    else:
        ans.append("wan mei!")
    print(" ".join(ans))


