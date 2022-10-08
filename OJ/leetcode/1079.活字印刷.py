# 题目：1079.活字印刷
# 难度：MEDIUM
# 最后提交：2022-09-14 13:09:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        v = set()
        for s in list(permutations(tiles)):
            for i in range(1<<n):
                t = ""
                for j in range(n):
                    if i>>j&1:
                        t += s[j]
                v.add(t)
        return len(v)-1