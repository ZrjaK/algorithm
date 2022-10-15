# 题目：2434.使用机器人打印字典序最小的字符串
# 难度：MEDIUM
# 最后提交：2022-10-09 10:44:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def robotWithString(self, s: str) -> str:
        st = []
        ss = list(s)[::-1]
        ans = ""
        c = [0] * 26
        for i in s:
            c[ord(i)-97] += 1
        while ss:
            while st and st[-1] <= ss[-1] and sum(c[:ord(st[-1])-97]) == 0:
                a = st.pop()
                ans += a
            a = ss.pop()
            c[ord(a)-97] -= 1
            st.append(a)
        while st:
            ans += st.pop()
        return ans