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


    # 以下操作全是暴力，寄希望于这里边元素不多。
    def add_interval(self,l,r,val):
        """区间挨个加
        """
        tree = self.tree
        begin = self.split(l)
        end = self.split(r+1)
        for i in range(begin,end):
            tree[i].v += val

    def query_max(self,l,r):
        """
        查找x,y区间的最小值
        """        
        begin = self.split(l)
        end = self.split(r+1)
        return max(node.v for node in self.tree[begin:end])
    def query_has_greater_than(self,l,r,val):
        """
        查找x,y区间是否有大于val的数
        """        
        begin = self.split(l)
        end = self.split(r+1)
        return any(node.v>val for node in self.tree[begin:end])
    
# 731. 我的日程安排表 II
# https://leetcode.cn/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.odt = ODT(0,10**9,0)


    def book(self, start: int, end: int) -> bool:
        if self.odt.query_has_greater_than(start,end-1,1) :
            return False
        self.odt.add_interval(start,end-1,1)
        return True
