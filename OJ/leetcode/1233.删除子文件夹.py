# 题目：1233.删除子文件夹
# 难度：MEDIUM
# 最后提交：2023-02-08 11:02:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        for i in range(len(folder)):
            folder[i] += "/"
        cur = 0
        ans = []
        i = cur + 1
        while i < len(folder):
            if folder[i].startswith(folder[cur]):
                i += 1
                continue
            ans.append(folder[cur][:-1])
            cur = i
            i = cur + 1
        ans.append(folder[cur][:-1])
        return ans
