for _ in range(int(input())):
    input()
    s = input()
    count = 0
    while "00" in s:
        s = s.replace("00", "0110", 1)
        count += 2
    while "010" in s:
        s = s.replace("010", "0110", 1)
        count += 1
    print(count)