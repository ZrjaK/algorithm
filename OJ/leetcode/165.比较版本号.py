# 题目：165.比较版本号
# 难度：MEDIUM
# 最后提交：2022-09-04 17:01:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = [int(i) for i in version1.split(".")]
        l2 = [int(i) for i in version2.split(".")]
        l1 += [0] * max(0, len(l2)-len(l1))
        l2 += [0] * max(0, len(l1)-len(l2))
        for i, j in zip(l1, l2):
            # print(i, j)
            if i > j:
                return 1
            elif j > i:
                return -1
        # print()
        return 0