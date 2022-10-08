# 题目：2274.不含特殊楼层的最大连续楼层数
# 难度：MEDIUM
# 最后提交：2022-05-15 10:38:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        h = [bottom-1]
        for i in special:
            if i > top:
                continue
            if i >= h[-1]:
                h.append(i)
        h.append(top+1)
        # print(h)
        ans = 0
        for i in range(1,len(h)):
            ans = max(ans, h[i]-h[i-1]-1)
        return ans