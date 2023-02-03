def calc(lst):
    for i in range(len(lst)):
        if lst[i][-1] == ",":
            if not lst[i].endswith("ong,"):
                return "Skipped"
    if not lst[-1].endswith("ong."):
        return "Skipped"
    lst[-3:] = ["qiao", "ben", "zhong."]
    return " ".join(lst)
for _ in range(int(input())):
    lst = input().split()
    print(calc(lst))