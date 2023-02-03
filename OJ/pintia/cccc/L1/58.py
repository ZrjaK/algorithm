a=input()
al=len(a)    #假设6的数量最多为字符串长度
for i in range(al,9,-1):
    if '6'*i in a:
        a=a.replace('6'*i,'27')    #替换9个以上的6
for i in range(9,3,-1):
    if '6'*i in a:
        a=a.replace('6'*i,'9')    #替换3-9个数量的6
print(a)    #输出修改好后的句子