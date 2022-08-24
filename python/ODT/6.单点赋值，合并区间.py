class ODTNode:
    def __init__(self,l,r,v):
        self.l,self.r,self.v = l,r,v
    def __lt__(self,other):
        return self.l<other.l
    def jiebao(self):
        return self.l,self.r,self.v
    # def __str__(self):
    #     return str((self.l,self.r,self.v))
    # def __repr__(self):
    #     return str((self.l,self.r,self.v))
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

    def query_all_intervals(self):
        tree = self.tree
        lines = []
        l = r = -1
        for node in tree :
            if node.v == 0:
                if l != -1:
                    lines.append([l,r])                    
                    l = -1
            else:
                if l == -1:
                    l = node.l 
                r = node.r
        # for line in lines:
        #     self.assign(line[0],line[1],1)
        # print(self.tree)
        return lines

# 352. 将数据流变为多个不相交区间
# https://leetcode.cn/problems/data-stream-as-disjoint-intervals/

class SummaryRanges:

    def __init__(self):
        self.odt = ODT(0,10**4+1,0)


    def addNum(self, val: int) -> None:
        self.odt.assign(val,val,1)


    def getIntervals(self) -> List[List[int]]:
        return self.odt.query_all_intervals()
