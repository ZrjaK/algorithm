# 题目：661.图片平滑器
# 难度：EASY
# 最后提交：2021-10-23 12:37:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        #padding
        m = len(img[0])
        N = [[0.5]+i+[0.5] for i in img]
        N = [[0.5]*(m+2)] + N + [[0.5]*(m+2)]
        
        #卷积
        for i in range(1,len(N)-1):
            for j in range(1,len(N[0])-1):
                total = [N[i-1][j-1],N[i][j-1],N[i+1][j-1],N[i-1][j],N[i][j],N[i+1][j],N[i-1][j+1],N[i][j+1],N[i+1][j+1]]
                sums,k = 0,0
                for _ in total:
                    if _ != 0.5:
                        sums += _
                    else:
                        k += 1
                img[i-1][j-1] = int(sums/(9-k))
        return img