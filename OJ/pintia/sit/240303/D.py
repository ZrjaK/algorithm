n = int(input())
a = [[float(i) for i in input().split()] for _ in range(n)]
A = [i[0] for i in a]
B = [i[1] for i in a]
A = [i / 10 - 5 for i in A]
A = [i if i >= 1 else 0 for i in A]
C = [i * j for i, j in zip(A, B)]
X = sum(C) / sum(B)
if X >= 4:
    print("Excellent")
elif X >= 3:
    print("Good")
elif X >= 2:
    print("Fair")
elif X >= 1:
    print("Pass")
else:
    print("Fail")
print("%.2f" % X)