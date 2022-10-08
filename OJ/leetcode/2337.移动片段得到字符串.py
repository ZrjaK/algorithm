# 题目：2337.移动片段得到字符串
# 难度：MEDIUM
# 最后提交：2022-07-10 10:52:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if [i for i in start if i != "_"] != [i for i in target if i != "_"]:
            return False
        n = len(start)
        a = b = 0
        for i in range(n):
            if start[i] == "R":
                a += 1
            if start[i] == "L":
                a -= 1
            if target[i] == "R":
                b += 1
            if target[i] == "L":
                b -= 1
            if a < b:
                return False
        return True
                