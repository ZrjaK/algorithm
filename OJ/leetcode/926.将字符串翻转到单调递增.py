# 题目：926.将字符串翻转到单调递增
# 难度：MEDIUM
# 最后提交：2022-07-09 01:19:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = s.count('0')   #分界点为0之前，统计之后的0
        res=[m]
        for x in s:
            if x=='1':   #如果是1，分界点之前1的个数+1，分界点之后0的个数不变
                m+=1
            else:       #如果是0，分界点之前1的个数不变，分界点之后0的个数减1
                m-=1
            res.append(m)        
        return min(res)