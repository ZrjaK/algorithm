# 题目：剑指 Offer II 033.变位词组
# 难度：MEDIUM
# 最后提交：2022-10-06 02:24:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(list(s)))].append(s)
        return list(d.values())