data = list(map(int, input().split()))
if data[2] >= data[0] and data[3] >= data[0]:
    print("{}-Y {}-Y".format(data[2], data[3]))
    print("huan ying ru guan")
elif data[2] < data[0] and data[3] >= data[1]:
    print("{}-Y {}-Y".format(data[2], data[3]))
    print("qing 2 zhao gu hao 1")
elif data[3] < data[0] and data[2] >= data[1]:
    print("{}-Y {}-Y".format(data[2], data[3]))
    print("qing 1 zhao gu hao 2")
elif data[2] < data[0] and data[1] > data[3] >= data[0]:
    print("{}-N {}-Y".format(data[2], data[3]))
    print("2: huan ying ru guan")
elif data[3] < data[0] and data[1] > data[2] >= data[0]:
    print("{}-Y {}-N".format(data[2], data[3]))
    print("1: huan ying ru guan")
else:
    print("{}-N {}-N".format(data[2], data[3]))
    print("zhang da zai lai ba")