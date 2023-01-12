# 题目：640.求解方程
# 难度：MEDIUM
# 最后提交：2023-01-03 01:35:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def solveEquation(self, equation: str) -> str:

        def check(st):
            a = b = i = 0
            m = len(st)
            while i < m:
                cur = st[i]
                while i + 1 < m and st[i + 1] not in "+-":
                    cur += st[i + 1]
                    i += 1
                # 更新系数
                if cur[-1] == "x":
                    cur = cur[:-1]
                    # 注意"+x"\"-x"\"x"的特殊情况
                    a += int(cur) if cur and cur not in "+-" else int(cur + "1")
                else:
                    b += int(cur)
                i += 1
            return [a, b]

        lst = equation.split("=")
        a1, b1 = check(lst[0])
        a2, b2 = check(lst[1])
        if a1 == a2:
            return "Infinite solutions" if b1 == b2 else "No solution"
        ans = (b2 - b1) // (a1 - a2)
        return f"x={ans}"