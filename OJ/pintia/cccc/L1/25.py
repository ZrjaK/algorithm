t = input()
if t[0] == " ":
    print("?", "+", t[1:] if t[1:].isdigit() and 1 <= int(t[1:]) <= 1000 else "?", "=", "?")
t = t.split()
print(t[0] if t[0].isdigit() and 1 <= int(t[0]) <= 1000 else "?", "+", 
    t[1] if t[1].isdigit() and 1 <= int(t[1]) <= 1000 else "?", "=",
    int(t[0]) + int(t[1]) if t[0].isdigit() and 1 <= int(t[0]) <= 1000
         and t[1].isdigit() and 1 <= int(t[1]) <= 1000 else "?")