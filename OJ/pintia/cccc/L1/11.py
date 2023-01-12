a = input()
b = input()
b = set(b)
print("".join([i for i in a if i not in b]))