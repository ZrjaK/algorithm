# 题目：1404.将二进制表示减到 1 的步骤数
# 难度：MEDIUM
# 最后提交：2022-03-25 20:45:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        while not s == "1":
            count += 1 
            if s[-1] == "0":
                s = s[:-1]
            else:
                for i in range(len(s)-1, -1, -1):
                    if s[i] == "0":
                        s = f'{s[:i]}1{s[i+1:]}'
                        break
                    else:
                        s = f'{s[:i]}0{s[i+1:]}'
                        if i == 0:
                            s = "1" + s
        return count