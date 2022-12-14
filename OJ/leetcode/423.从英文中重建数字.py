# 题目：423.从英文中重建数字
# 难度：MEDIUM
# 最后提交：2022-04-29 21:10:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def originalDigits(self, s: str) -> str:
        n0 = s.count('z')
        n2 = s.count('w')
        n8 = s.count('g')
        n6 = s.count('x')
        n3 = s.count('t') - n2 - n8
        n4 = s.count('r') - n3 - n0
        n7 = s.count('s') - n6
        n1 = s.count('o') - n4 - n2 - n0
        n5 = s.count('v') - n7
        n9 = s.count('i') - n8 - n6 - n5
        
        ns = (n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
        
        return "".join((str(i)*n for i, n in enumerate(ns)))