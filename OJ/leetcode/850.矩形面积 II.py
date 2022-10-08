# 题目：850.矩形面积 II
# 难度：HARD
# 最后提交：2022-09-16 13:35:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ps = []
        for x1, _, x2, _ in rectangles:
            ps.append(x1)
            ps.append(x2)
        ps.sort()
        ans = 0
        for i in range(1, len(ps)):
            a, b = ps[i - 1], ps[i]
            w = b - a
            if w == 0:
                continue
            odt = ODT(0, 10**9, 0)
            for x1, y1, x2, y2 in rectangles:
                if x1 <= a and x2 >= b:
                    odt.assign(y1, y2-1, 1)
            ans += w * odt.query_sum(0, 10**9)
        return ans % int(1e9+7)

class ODTNode:
    __slots__ = ['l','r','v']
    def __init__(self,l,r,v):
        self.l,self.r,self.v = l,r,v
    def __lt__(self,other):
        return self.l<other.l
    def jiebao(self):
        return self.l,self.r,self.v
class ODT:
    def __init__(self,l,r,v):
        from sortedcontainers import SortedList
        self.tree = SortedList([ODTNode(l,r,v)])
        

    def split(self,pos):
        """ 在pos位置切分，返回左边界l为pos的线段下标
        """
        tree = self.tree
        p = tree.bisect_left(ODTNode(pos,0,0))
        if p != len(tree) and tree[p].l == pos:
            return p 
        p -= 1
        l,r,v = tree[p].jiebao()
        tree[p].r = pos-1
        # tree.pop(p)
        # tree.add(ODTNode(l,pos-1,v))
        tree.add(ODTNode(pos,r,v))
        return p+1
       
    def assign(self,l,r,v):
        """
        把[l,r]区域全变成val
        """
        tree = self.tree
        begin = self.split(l)
        end = self.split(r+1)
        del tree[begin:end]
        tree.add(ODTNode(l,r,v))


    def query_sum(self,l,r):
        """
        查找x,y区间的最大值
        """        
        begin = self.split(l)
        end = self.split(r+1)
        return sum(node.v * (node.r-node.l+1) for node in self.tree[begin:end])