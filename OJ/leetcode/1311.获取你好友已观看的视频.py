# 题目：1311.获取你好友已观看的视频
# 难度：MEDIUM
# 最后提交：2022-08-08 17:53:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        used = [False] * n
        q = collections.deque([id])
        used[id] = True
        for _ in range(level):
            span = len(q)
            for i in range(span):
                u = q.popleft()
                for v in friends[u]:
                    if not used[v]:
                        q.append(v)
                        used[v] = True
        
        freq = collections.Counter()
        for _ in range(len(q)):
            u = q.pop()
            for watched in watchedVideos[u]:
                freq[watched] += 1

        videos = list(freq.items())
        videos.sort(key=lambda x: (x[1], x[0]))

        ans = [video[0] for video in videos]
        return ans