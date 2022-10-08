# 题目：49.字母异位词分组
# 难度：MEDIUM
# 最后提交：2022-08-27 13:31:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        f = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        for s in strs:
            t = 1
            for i in s:
                t *= f[ord(i)-97]
            d[t].append(s)
        return list(d.values())
