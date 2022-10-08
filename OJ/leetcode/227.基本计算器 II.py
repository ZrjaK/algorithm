# 题目：227.基本计算器 II
# 难度：MEDIUM
# 最后提交：2022-09-02 12:14:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        stack=[]
        num=[]
        operator=['+','-','*','/']
        cur=''
        for i in s:
            if i not in operator:
                cur+=i
            else:
                num.append(int(cur))
                if stack and stack[-1] in ['*','/']:
                    t=stack.pop()
                    b,a=num.pop(),num.pop()
                    if t=='*':
                        num.append(a*b)
                    else:
                        num.append(a//b)
                    stack.append(i)
                else:
                    stack.append(i)
                cur=''
        num.append(int(cur))
        if stack and stack[-1] in ['*','/']:
            t=stack.pop()
            b,a=num.pop(),num.pop()
            if t=='*':
                num.append(a*b)
            if t=='/':
                num.append(a//b)
        
       
        stack=stack[::-1]
        num=num[::-1]
        while stack:
            t=stack.pop()
            a,b=num.pop(),num.pop()
            if t=='-':
                num.append(a-b)
            if t=='+':
                num.append(a+b)
        return num[0]