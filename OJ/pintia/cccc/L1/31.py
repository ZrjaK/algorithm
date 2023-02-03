for _ in range(int(input())):
    H, W = map(int, input().split())
    t = (H - 100) * 0.9 * 2
    if abs(W-t) < t * 0.1:
        print("You are wan mei!")
    elif W < t:
        print("You are tai shou le!")
    else:
        print("You are tai pang le!")