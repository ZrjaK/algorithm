# 题目：2165.重排数字的最小值
# 难度：MEDIUM
# 最后提交：2022-09-01 16:29:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num:
            return 0
        d = defaultdict(int)
        for i in str(num):
            d[i] += 1
        ans = ""
        if num > 0:
            for i in range(1, 10):
                t = str(i)
                if d[t]:
                    ans += t
                    d[t] -= 1
                    break
            for i in range(10):
                t = str(i)
                ans += t * d[t]
            return int(ans)
        else:
            for i in range(9, 0, -1):
                t = str(i)
                if d[t]:
                    ans += t
                    d[t] -= 1
                    break
            for i in range(9, -1, -1):
                t = str(i)
                ans += t * d[t]
            return -int(ans)