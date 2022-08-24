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
        查找x,y区间的最大值
        """        
        begin = self.split(l)
        end = self.split(r+1)
        return max(node.v for node in self.tree[begin:end])
    def query_all_max(self,):
        """
        查找x,y区间的最大值
        """        
        begin = self.split(0)
        end = self.split(10**9+1)
        return max(node.v for node in self.tree[begin:end])

# 699. 掉落的方块
# https://leetcode.cn/problems/falling-squares/

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        odt = ODT(1,10**9,0) 
        ans = []
        m = 0
        for l,d in positions:
            h = odt.query_max(l,l+d-1)
            odt.assign(l,l+d-1,h+d)
            m = max(m,h+d)
            ans.append(m)
        return ans

