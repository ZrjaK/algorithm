# 题目：2284.最多单词数的发件人
# 难度：MEDIUM
# 最后提交：2022-05-28 22:42:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        ans = senders[0]
        for m, s in zip(messages, senders):
            t = m.split(" ")
            d[s] += len(t)
            if d[s] > d[ans]:
                ans = s
            elif d[s] == d[ans]:
                if s > ans:
                    ans = s
        return ans