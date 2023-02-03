s = input()
if len(s) == 6:
    exit(print(s[:4] + "-" + s[4:]))
if int(s[:2]) < 22:
    print("20" + s[:2] + "-" + s[2:])
else:
    print("19" + s[:2] + "-" + s[2:])