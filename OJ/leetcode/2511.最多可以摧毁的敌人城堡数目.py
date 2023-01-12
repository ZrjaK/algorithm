# 题目：2511.最多可以摧毁的敌人城堡数目
# 难度：EASY
# 最后提交：2022-12-24 22:34:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        n = len(forts)
        for i in range(n):
            if forts[i] in [1, -1]:
                t = 0
                for j in range(i+1, n):
                    if forts[j] + forts[i] == 0:
                        ans = max(ans, t)
                        break
                    if forts[j] == forts[i]:
                        break
                    else:
                        t += 1
        return ans