s1 = s2 = ""
a1 = input()
a2 = input()
for i in range(1,len(a1)):
    if int(a1[i]) % 2 == int(a1[i - 1]) % 2:
        s1 += max(a1[i], a1[i - 1])

for i in range(1,len(a2)):
    if int(a2[i]) % 2 == int(a2[i - 1]) % 2:
        s2 += max(a2[i], a2[i - 1])
if s1 == s2:
    print(s1)
else:
    print(s1)
    print(s2)
