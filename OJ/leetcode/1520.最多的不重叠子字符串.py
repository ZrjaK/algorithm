# 题目：1520.最多的不重叠子字符串
# 难度：HARD
# 最后提交：2022-10-11 11:00:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        o = [ord(i)-97 for i in s]
        f = [[1e99, -1] for _ in range(26)]
        for i in range(n):
            f[o[i]][1] = i
            f[o[i]][0] = min(f[o[i]][0], i)
        h = [-1] * 26
        res = []
        for j in range(26):
            l = f[j][0]
            r = f[j][1]
            if l == 1e99 or r == -1:
                continue
            i = l
            while i < r:
                r = max(r, f[o[i]][1])
                if f[o[i]][0] < l:
                    break
                i += 1
            else:
                res.append([l, r])
        res.sort(key=lambda x: (x[1], x[1]-x[0]))
        c = -1
        ans = []
        for l, r in res:
            if l > c:
                ans.append(s[l:r+1])
                c = r
        return ans