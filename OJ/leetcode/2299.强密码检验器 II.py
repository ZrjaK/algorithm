# 题目：2299.强密码检验器 II
# 难度：EASY
# 最后提交：2023-01-19 00:51:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        d1 = [chr(i) for i in range(65, 65+26)]
        d2 = [chr(i) for i in range(97, 97+26)]
        d3 = [str(i) for i in range(10)]
        d4 = list("!@#$%^&*()-+")
        t1 = False
        for i in d1:
            if i in password:
                t1= True
        t2= False
        for i in d2:
            if i in password:
                t2= True
        t3= False
        for i in d3:
            if i in password:
                t3= True
        t4= False
        for i in d4:
            if i in password:
                t4= True
        t5 = False
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                t5= True
        return t1 and t2 and t3 and t4 and not t5