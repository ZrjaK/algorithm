# 题目：1024.视频拼接
# 难度：MEDIUM
# 最后提交：2022-07-12 01:50:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x:x[1])
        clips.sort(key=lambda x:x[0])
        start = [i[0] for i in clips]
        starts = set(start)
        @cache
        def p(t):
            if t >= time:
                return 0
            if t not in starts:
                return 1e99
            res = 1e99
            for i in range(bisect_left(start, t), bisect_right(start, t)):
                for j in range(t+1, clips[i][1]+1):
                    res = min(res, p(j))
            return res + 1
        res = p(0)
        return res if res < 1e90 else -1