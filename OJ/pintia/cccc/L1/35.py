h = []
while 1:
    s = input()
    if s == ".":
        break
    h.append(s)
if len(h) < 2:
    print("Momo... No one is for you ...")
elif len(h) < 14:
    print(f"{h[1]} is the only one for you...")
else:
    print(f"{h[1]} and {h[13]} are inviting you to dinner...")