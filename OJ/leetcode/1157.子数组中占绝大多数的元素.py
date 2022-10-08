# 题目：1157.子数组中占绝大多数的元素
# 难度：HARD
# 最后提交：2022-09-24 11:04:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MajorityChecker:

    def __init__(self, arr: List[int]):
        class Node:
            def __init__(self, i, j):
                self.l = i
                self.r = j
                if i + 1 == j:
                    self.k = arr[i]
                    self.c = 1
                    return
                mid = (i + j) // 2
                self.left = Node(i, mid)
                self.right = Node(mid, j)
                self.build()
                
            def build(self):#摩尔投票
                if self.left.k == self.right.k:
                    self.k = self.left.k
                    self.c = self.left.c + self.right.c
                else:
                    if self.left.c > self.right.c:
                        self.k = self.left.k
                        self.c = self.left.c - self.right.c
                    else:
                        self.k = self.right.k
                        self.c = self.right.c - self.left.c
                        
            def find(self, i, j):
                if self.l == i and self.r == j:
                    return self.k, self.c
                mid = (self.l + self.r) // 2
                if mid >= j:
                    return self.left.find(i, j)
                elif mid <= i:
                    return self.right.find(i, j)
                else:
                    left = self.left.find(i, mid)
                    right = self.right.find(mid, j)
                    if left[0] == right[0]:
                        return left[0], left[1] + right[1]
                    else:
                        if left[1] > right[1]:
                            return left[0], left[1] - right[1]
                        else:
                            return right[0], right[1] - left[1]
                        
        self.node = Node(0, len(arr))
        self.d = {}
        for i, n in enumerate(arr):
            if n not in self.d:#将数值映射为索引列表
                self.d[n] = []
            self.d[n].append(i)
                


    def query(self, left: int, right: int, threshold: int) -> int:
        n, c = self.node.find(left, right + 1)
        c = bisect.bisect_right(self.d[n], right) - bisect.bisect_left(self.d[n], left)#通过二分找到区间内的数量
        return n if c >= threshold else -1



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
