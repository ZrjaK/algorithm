# 题目：672.灯泡开关 Ⅱ
# 难度：MEDIUM
# 最后提交：2022-09-15 00:04:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        s1 = s2 = s3 = s4 = 0
        for i in range(n):
            s1 ^= (1<<i)
            if (i+1)%2==0: s2 ^= (1<<i)
            if (i+1)%2==1: s3 ^= (1<<i)
            if (i+1)%3==1: s4 ^= (1<<i)
        print(s1,s2,s3,s4)
        vis = set([s1])
        for _ in range(presses):
            states = set()
            for s in vis:
                for switch in [s1, s2, s3, s4]:
                    states.add(s ^ switch)
            vis = states
        return len(vis)