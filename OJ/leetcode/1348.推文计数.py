# 题目：1348.推文计数
# 难度：MEDIUM
# 最后提交：2022-05-06 01:02:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class TweetCounts:

    def __init__(self):
        self.d = defaultdict(list)
        self.h = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.d[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        f = self.h[freq]
        self.d[tweetName].sort()
        res = []
        for i in range(startTime, endTime+1, f):
            l = bisect_left(self.d[tweetName], i)
            r = bisect_right(self.d[tweetName], min(endTime, i+f-1))
            # print(self.d[tweetName], i, l, r)
            res.append(r-l)
        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)