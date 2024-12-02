input()
down,left, up, right = False, False, False, True
x, y = 0, 0
for s in input():
    if s == "S":
        if left:
            x -= 1
        if right:
            x += 1
        if up:
            y += 1
        if down:
            y -= 1
    if s == "R":
        left, up, right, down = down, left, up, right
print(x, y)