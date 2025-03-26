S = input()
if len(set(S)) == 1 or all((int(S[i]) + 1) % 10 == int(S[i + 1]) for i in range(3)):
    print("Weak")
else:
    print("Strong")