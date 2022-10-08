# 题目：833.字符串中的查找与替换
# 难度：MEDIUM
# 最后提交：2022-08-29 14:27:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)
        for i, j, k in sorted(zip(indices, sources, targets)):
            # print(i, j, k)
            # print(ans)
            if s[i:i+len(j)] == j:
                ans = ans[:i] + [k] + [""] * (len(j)-1) + ans[i+len(j):]
        return "".join(ans)