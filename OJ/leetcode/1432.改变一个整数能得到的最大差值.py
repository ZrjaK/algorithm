# 题目：1432.改变一个整数能得到的最大差值
# 难度：MEDIUM
# 最后提交：2022-09-07 09:03:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDiff(self, num: int) -> int:
        s1 = list(str(num))
        t = ""
        for i in s1:
            if i != "9":
                t = i
                break
        for i in range(len(s1)):
            if s1[i] == t:
                s1[i] = "9"
        s2 = list(str(num))
        t = ""
        c = s2[0]
        for i in s2:
            if i == c == "1" or i == "0":
                continue
            t = i
            break
        for i in range(len(s2)):
            if s2[i] == t:
                if t == c:
                    s2[i] = "1"
                else:
                    s2[i] = "0"
        return int("".join(s1)) - int("".join(s2))
