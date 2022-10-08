# 题目：830.较大分组的位置
# 难度：EASY
# 最后提交：2021-10-24 15:47:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s += "A"
        i = 0
        res = []
        while i < len(s):
            for j in range(i+1, len(s)):
                if s[j-1:j] != s[j:j+1]:
                    if len(s[i:j]) >= 3:
                        res.append([i, j - 1])
                    i = j
                    break
                
            else:
                i += 1
                
        return res


