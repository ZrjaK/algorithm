# 题目：1096.花括号展开 II
# 难度：HARD
# 最后提交：2022-09-29 21:53:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def f(s1, s2):#用于处理相接表达式
            res = set()
            for i in s1:
                for j in s2:
                    res.add(i + j)
            return res
        def dfs(expression):
            last = ","
            res = set()#结果集合
            tmp = set()#缓存集合
            i = 0
            while i < len(expression):
                if expression[i] == ",":#如果是逗号，说明上一个相接表达式已结束，将tmp并至res
                    res |= tmp
                    tmp = set()
                    i += 1
                elif expression[i] == "{":#如果是花括号，需要单独处理
                    l = 1#左括号数量
                    r = 0#右括号数量
                    j = i + 1
                    while l > r:#直至左右括号数量相等为止
                        if expression[j] == "{":
                            l += 1
                        elif expression[j] == "}":
                            r += 1
                        j += 1
                    if last == ",":#如果上一个字符是逗号，说明要取并集
                        tmp |= dfs(expression[i + 1:j - 1])
                    else:#否则则是相接表达式
                        tmp = f(tmp, dfs(expression[i + 1:j - 1]))
                    i = j
                    last = "}"
                else:
                    n = ""#变量名
                    while i < len(expression) and expression[i] not in ",{":
                        n += expression[i]
                        i += 1
                    if last == ",":#如果不是相接表达式
                        tmp.add(n)
                    else:#是相接表达式
                        tmp = {x + n for x in tmp}
                last = expression[i - 1]#更新上一个字符
            return res | tmp
        return sorted(dfs(expression))