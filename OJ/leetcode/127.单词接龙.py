# 题目：127.单词接龙
# 难度：HARD
# 最后提交：2022-10-10 17:01:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        d = defaultdict(set)
        for i in range(len(beginWord)):
            for j in range(97, 97+26):
                if ord(beginWord[i]) != j:
                    t = beginWord[:i] + chr(j) + beginWord[i+1:]
                    if t in s:
                        d[beginWord].add(t)
                        d[t].add(beginWord)
        for w in wordList:
            for i in range(len(w)):
                for j in range(97, 97+26):
                    if ord(w[i]) != j:
                        t = w[:i] + chr(j) + w[i+1:]
                        if t in s:
                            d[w].add(t)
                            d[t].add(w)
        q = deque([[1, beginWord]])
        v = set()
        while q:
            s, t = q.popleft()
            if t == endWord:
                return s
            if t in v:
                continue
            v.add(t)
            for nxt in d[t]:
                q.append((s+1, nxt))
        return 0