# 题目：2269.找到一个数字的 K 美丽值
# 难度：EASY
# 最后提交：2022-05-14 22:33:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(0,len(s)-k+1):
            t = int(s[i:i+k])
            if t == 0:
                continue
            if num % t == 0:
                ans += 1
        return ans