s = [int(i) for i in input()]
arr = set(s)
arr = sorted(arr)[::-1]
idx = [arr.index(i) for i in s]
    
print(f"""int[] arr = new int[]{'{' + ','.join(map(str, arr)) + '}'};
int[] index = new int[]{'{' + ','.join(map(str, idx)) + '}'};""")