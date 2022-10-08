# 题目：2381.字母移位 II
# 难度：MEDIUM
# 最后提交：2022-08-21 00:17:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for x, y, z in shifts:
            if z:
                diff[x] += 1
                diff[y+1] -= 1
            else:
                diff[x] -= 1
                diff[y+1] += 1
        ans = []
        pos = 0
        for idx, char in enumerate(s):
            pos += diff[idx]
            tmp = chr((ord(char) + pos - ord('a')) % 26 + ord('a'))
            ans.append(tmp)
        return ''.join(ans)