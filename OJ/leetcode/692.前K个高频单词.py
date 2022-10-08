# 题目：692.前K个高频单词
# 难度：MEDIUM
# 最后提交：2022-08-27 23:55:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return sorted(list(c.keys()), reverse=True,
                key=lambda x:(-c[x], x))[-k:][::-1]