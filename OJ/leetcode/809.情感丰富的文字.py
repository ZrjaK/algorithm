# 题目：809.情感丰富的文字
# 难度：MEDIUM
# 最后提交：2022-11-25 08:41:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        get = lambda x: [(ch, len(tuple(seq))) for ch, seq in groupby(x)]
        ori, cnt = get(s), 0

        for mini in map(get, words):
            if len(ori) != len(mini): continue
            if any(c1 != c2 or s2 > s1 or s2 < s1 < 3
                   for (c1, s1), (c2, s2) in zip(ori, mini)):
                continue
            cnt += 1
        
        return cnt