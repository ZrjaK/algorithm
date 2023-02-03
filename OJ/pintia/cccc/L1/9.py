from fractions import Fraction

ans = Fraction(0)
n = int(input())
for i in input().split():
    ans += Fraction(i)
s1, s2 = ans.numerator, ans.denominator
if s1 > s2 and ans != int(ans):
    print(s1 // s2, Fraction(ans - s1 // s2))
else:
    print(ans)