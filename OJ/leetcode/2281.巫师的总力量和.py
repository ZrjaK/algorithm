# 题目：2281.巫师的总力量和
# 难度：HARD
# 最后提交：2022-05-22 12:26:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(strength)
        left, st = [-1] * n, []  # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        for i, v in enumerate(strength):
            while st and strength[st[-1]] >= v: st.pop()
            if st: left[i] = st[-1]
            st.append(i)

        right, st = [n] * n, []  # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        for i in range(n - 1, -1, -1):
            while st and strength[st[-1]] > strength[i]: st.pop()
            if st: right[i] = st[-1]
            st.append(i)

        s = [0] * (n + 1)  # 前缀和
        for i, v in enumerate(strength):
            s[i + 1] = (s[i] + v) % MOD
        ss = [0] * (n + 2)  # 前缀和的前缀和
        for i, v in enumerate(s):
            ss[i + 1] = (ss[i] + v) % MOD

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            res = ((i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])) % MOD
            ans = (ans + res * v) % MOD  # 累加贡献
        return ans