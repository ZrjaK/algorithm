# 题目：2271.毯子覆盖的最多白色砖块数
# 难度：MEDIUM
# 最后提交：2022-05-14 23:09:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x:x[0])
        n = len(tiles)
        h = [tiles[0][1]-tiles[0][0]+1]
        for i in range(1,n):
            h.append(h[-1]+tiles[i][1]-tiles[i][0]+1)
        # print(h)
        l = [i[0] for i in tiles]
        ans = 0
        for i in range(n):
            t = bisect_left(l, tiles[i][1]-carpetLen+1)
            if t == 0:
                ans = max(ans, h[i])
                continue
            if t == i+1:
                ans = max(ans, carpetLen)
                # continue
            f = h[i]-h[t-1]
            a = tiles[t-1][1] - (tiles[i][1]-carpetLen)
            if a > 0:
                f += a
            ans = max(ans, f)
        return ans