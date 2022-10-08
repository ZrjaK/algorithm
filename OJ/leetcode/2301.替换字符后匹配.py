# 题目：2301.替换字符后匹配
# 难度：HARD
# 最后提交：2022-06-11 23:00:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = defaultdict(set)
        for i, j in mappings:
            d[i].add(j)
        n = len(sub)
        
        def check(p):
            i = j = 0
            while i < n:
                if p[i] == sub[j]:
                    i += 1
                    j += 1
                    continue
                if p[i] in d[sub[j]]:
                    i += 1
                    j += 1
                else:
                    return False
            return True
            
        for i in range(0, len(s)-n+1):
            t = s[i:i+n]
            if check(t):
                return True
        return False