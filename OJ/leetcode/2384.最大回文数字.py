# 题目：2384.最大回文数字
# 难度：MEDIUM
# 最后提交：2022-08-21 10:54:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestPalindromic(self, num: str) -> str:
        if num.count("0") == len(num):
            return "0"
        d = defaultdict(int)
        for i in num:
            d[i] += 1
        ans = ""
        for i in range(9, -1, -1):
            if d[str(i)] > 1:
                t = d[str(i)] // 2
                d[str(i)] -= 2 * t
                ans += str(i) * t
        c = -1
        for i in range(len(ans)):
            if ans[i] != "0":
                c = i
                break
       
        ans = ans[c:]
        if c == -1:
            ans = ""
        t = ans[::-1]
        for i in range(9, -1, -1):
            if d[str(i)]:
                ans += str(i)
                break
        
        ans += t
        return ans