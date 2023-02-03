a, b = map(int, input().split())
sb = b if b >= 0 else ("(" + str(b) + ")")
sc = "Error" if b == 0 else "%.2f" % (a / b)
print(f"{a}/{sb}={sc}")