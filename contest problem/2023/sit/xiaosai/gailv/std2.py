from math import factorial

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0

def P(a, b):
    return comb(8, a) * comb(8, b) * comb(8, 12 - a - b) / comb(24, 12)

p840 = 6 * P(8, 4); e840 = p840 * 100
p831 = 6 * P(8, 3); e831 = p831 * 10
p822 = 3 * P(8, 2); e822 = p822 * 10

p750 = 6 * P(7, 5); e750 = p750 * 20
p741 = 6 * P(7, 4); e741 = p741 * 2
p732 = 6 * P(7, 3); e732 = p732 * 2

p660 = 3 * P(6, 6); e660 = p660 * 20
p651 = 6 * P(6, 5); e651 = p651 * 1
p642 = 6 * P(6, 4); e642 = p642 * 1
p633 = 3 * P(6, 3); e633 = p633 * 1

p552 = 3 * P(5, 5); e552 = p552 * 1

p444 = 1 * P(4, 4); e444 = p444 * 1

p543 = 6 * P(5, 4); e543 = p543 * -10

ans = e840 + e831 + e822 + e750 + e741 + e732 + e660 + e651 + e642 + e633 + e552 + e444 + e543
print(ans)
