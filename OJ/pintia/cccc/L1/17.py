ans = 1
n = int(input())
if n < 0:
    ans *= 1.5
    n *= -1
ans *= str(n).count("2") / len(str(n))
if n % 2 == 0:
    ans *= 2
ans *= 100
print("%.2f" % ans + "%")