# 题目：835.图像重叠
# 难度：MEDIUM
# 最后提交：2022-09-12 13:45:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)
        img1 = [int("".join([str(j) for j in i]), 2) for i in img1]
        img2 = [int("".join([str(j) for j in i]), 2) for i in img2]
        for i in range(n):
            for j in range(n):
                ans = max(ans, 
                    sum([(img1[k] & img2[k-i]>>j).bit_count() for k in range(i, n)]), 
                    sum([(img1[k] & img2[k-i]<<j).bit_count() for k in range(i, n)]),
                    sum([(img2[k] & img1[k-i]>>j).bit_count() for k in range(i, n)]), 
                    sum([(img2[k] & img1[k-i]<<j).bit_count() for k in range(i, n)]))
        return ans