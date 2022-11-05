# 题目：784.字母大小写全排列
# 难度：MEDIUM
# 最后提交：2022-10-30 00:20:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        b = 0
        for i in range(n):
            if ord("0") <= ord(s[i]) <= ord("9"):
                b |= 1<<i
        for i in range(1<<n):
            if i & b != b:
                continue
            t = ""
            for j in range(n):
                if 1<<j & i:
                    t += s[j].upper()
                else:
                    t += s[j].lower()
            ans.append(t)
        return ans