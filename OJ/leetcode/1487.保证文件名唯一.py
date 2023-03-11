# 题目：1487.保证文件名唯一
# 难度：MEDIUM
# 最后提交：2023-03-03 00:58:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        index = {}
        for name in names:
            if name not in index:
                ans.append(name)
                index[name] = 1
            else:
                k = index[name]
                while name + '(' + str(k) + ')' in index:
                    k += 1
                t = name + '(' + str(k) + ')'
                ans.append(t)
                index[name] = k + 1
                index[t] = 1
        return ans
