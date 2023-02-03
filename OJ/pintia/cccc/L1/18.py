s = input()
t = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
t = (t - 1 + 60) // 60 - 12
if t <= 0:
    print(f"Only {s}.  Too early to Dang.")
else:
    print("Dang" * t)
