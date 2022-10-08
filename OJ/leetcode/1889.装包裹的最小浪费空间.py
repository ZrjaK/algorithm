# 题目：1889.装包裹的最小浪费空间
# 难度：HARD
# 最后提交：2022-09-25 23:01:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n, m = len(packages), len(boxes)
        packages.sort()
        h = list(accumulate(packages)) + [0]
        for i in range(m):
            boxes[i] = [0] + sorted(boxes[i])
        boxes.sort(key=lambda x: -x[-1])
        ans = 1e99
        for arr in boxes:
            if arr[-1] < packages[-1]:
                break
            tt = 0
            for i in range(1, len(arr)):
                l = bisect_right(packages, arr[i-1])
                r = bisect_right(packages, arr[i])
                tt += (r-l) * arr[i] - (h[r-1] - h[l-1])
            ans = min(ans, tt)
        return ans % int(1e9+7) if ans < 1e90 else -1