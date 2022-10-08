# 题目：832.翻转图像
# 难度：EASY
# 最后提交：2021-10-25 14:54:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [i[::-1] for i in image]
        for i in image:
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                elif i[j] == 1:
                    i[j] = 0
        return image
        