# 题目：893.特殊等价字符串组
# 难度：MEDIUM
# 最后提交：2022-10-18 16:57:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def calc(w):
            o = sorted(list(w[1::2]), reverse=True)
            e = sorted(list(w[::2]), reverse=True)
            r = []
            while o and e:
                r.append(e.pop())
                r.append(o.pop())
            r += o + e
            return "".join(r)
        n = len(words)
        d = defaultdict(int)
        for w in words:
            d[calc(w)] += 1
        return len(d.keys())