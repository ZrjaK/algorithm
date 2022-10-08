# 题目：2276.统计区间中的整数数目
# 难度：HARD
# 最后提交：2022-09-26 11:44:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class CountIntervals:

    def __init__(self):
        self.odt = ODT(1, 10**9, 0)

    def add(self, left: int, right: int) -> None:
        self.odt.assign(left, right, 1)

    def count(self) -> int:
        return self.odt.cnt

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
        self.cnt = 0
        

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
        for i in range(begin, end):
            t = tree[i].jiebao()
            if t[2]:
                self.cnt -= t[1] - t[0] + 1
        del tree[begin:end]
        # for i in range(begin,end):
        #     tree.pop(begin)
        tree.add(ODTNode(l,r,v))
        self.cnt += r-l+1

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()