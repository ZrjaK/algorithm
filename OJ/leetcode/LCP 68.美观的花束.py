# 题目：LCP 68.美观的花束
# 难度：MEDIUM
# 最后提交：2022-10-07 15:16:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = 0
        d = defaultdict(int)
        c = -1
        l = 0
        n = len(flowers)
        for r in range(n):
            d[flowers[r]] += 1
            if d[flowers[r]] > cnt:
                c = flowers[r]
            while c != -1:
                d[flowers[l]] -= 1
                if d[c] <= cnt:
                    c = -1
                l += 1
            ans += r-l+1
        return ans % int(1e9+7)