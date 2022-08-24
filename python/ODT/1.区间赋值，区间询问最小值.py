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
        # for i in range(begin,end):
        #     tree.pop(begin)
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

    def query_min(self,l,r):
        """
        查找x,y区间的最小值
        """        
        begin = self.split(l)
        end = self.split(r+1)
        return min(node.v for node in self.tree[begin:end])
    def query_kth(self,l,r,k):
        """查找[x,y]区间第k小的数
        """
        begin = self.split(l)
        end = self.split(r+1)
        vs = [(node.v,node.r-node.l+1) for node in self.tree[begin:end]]  # v和v的个数，排序
        for v,d in sorted(vs):  # 挨个往外丢，缩小k
            k -= d 
            if k <= 0:
                return v 
    def query_sum_of_pow(self,l,r,x):
        """求区间x次方的和，一般还得mod，那就要手写快速幂
        """
        s = 0
        begin = self.split(l)
        end = self.split(r+1)
        for node in self.tree[begin:end]:
            s += (node.v**x) * (node.r-node.l+1)
        return s

# 715. Range 模块
# https://leetcode.cn/problems/range-module/

class RangeModule:

    def __init__(self):
        self.tree = ODT(1,10**9,0)


    def addRange(self, left: int, right: int) -> None:
        self.tree.assign(left,right-1,1)


    def queryRange(self, left: int, right: int) -> bool:
        return 1 == self.tree.query_min(left,right-1)


    def removeRange(self, left: int, right: int) -> None:
        self.tree.assign(left,right-1,0)
