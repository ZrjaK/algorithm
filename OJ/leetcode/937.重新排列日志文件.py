# 题目：937.重新排列日志文件
# 难度：MEDIUM
# 最后提交：2021-11-03 11:53:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l1=[]
        l2=[]
        for l in logs:
            if l[-1].isalpha():
                l1.append(l)
            else:
                l2.append(l)
        l1.sort(key=lambda x:(x[x.index(' ')+1:],x[:x.index(' ')+1]))
        return l1+l2