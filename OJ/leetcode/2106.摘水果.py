# 题目：2106.摘水果
# 难度：HARD
# 最后提交：2022-09-17 10:27:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        h = [0] * (1+max(startPos+k, max(i[0] for i in fruits)))
        for i, j in fruits:
            h[i] = j
        for i in range(1, len(h)):
            h[i] += h[i-1]
        h += [0]
        ans = 0
        for i in range(k+1):
            ans = max(ans, h[max(startPos, startPos+k-2*i)]-h[max(0, startPos-i)-1], 
                            h[startPos+i]-h[max(0, startPos-(k-2*i))-1])
        return ans