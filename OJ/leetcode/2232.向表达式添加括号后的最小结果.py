# 题目：2232.向表达式添加括号后的最小结果
# 难度：MEDIUM
# 最后提交：2022-04-10 10:54:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeResult(self, expression: str) -> str:
        n1, n2 = expression.split("+")
        ans = int(n1)+int(n2)
        ansexp = f'({n1}+{n2})'
        for i in range(0,len(n1)):
            left1 = n1[:i]
            left2 = int(n1[i:])
            for j in range(1,len(n2)+1):
                right1 = int(n2[:j])
                right2 = n2[j:]
                if not right2:
                    right2 = 1
                if not left1:
                    left1 = 1
                t = int(left1)*int(left2+right1)*int(right2)
                if ans > t:
                    ans = t
                    if right2 == 1:
                        right2 = ""
                    if left1 == 1:
                        left1 = ""
                    ansexp = f'{left1}({left2}+{right1}){right2}'
        return ansexp