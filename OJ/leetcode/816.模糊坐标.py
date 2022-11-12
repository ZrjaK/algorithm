# 题目：816.模糊坐标
# 难度：MEDIUM
# 最后提交：2022-11-07 07:32:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def p(t):
            ans = []
            for i in range(1, len(t)):
                if str(int(t[:i])) == t[:i] and t[i:] == t[i:].rstrip("0") and not all(j == "0" for j in t[i:]):
                    ans.append(t[:i] + "." + t[i:])
            if str(int(t)) == t:
                ans.append(t)
            return ans
        ans = []
        s = s[1:-1]
        for i in range(1, len(s)):
            x = p(s[:i])
            y = p(s[i:])
            for i in x:
                for j in y:
                    ans.append('(' + i + ', ' + j + ')')
        return ans