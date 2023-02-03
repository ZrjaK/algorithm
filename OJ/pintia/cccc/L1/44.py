k = int(input())
i = 0
d = ["ChuiZi", "JianDao", "Bu"]
while 1:
    s = input()
    if s == "End":
        break
    if i == k:
        print(s)
        i = 0
        continue
    t = d.index(s)
    print(d[(t-1)%3])
    i += 1