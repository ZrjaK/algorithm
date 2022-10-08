# 题目：218.天际线问题
# 难度：HARD
# 最后提交：2022-08-24 00:10:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key=lambda x:x[2])
        odt = ODT(0, 1<<31, 0)
        for l, r, h in buildings:
            odt.assign(l, r-1, h)
        # for i in odt.tree:
        #     print(i.jiebao())
        if odt.tree[0].jiebao()[2] == 0:
            odt.tree.pop(0)
        ans = []
        c = 0
        for i in odt.tree:
            t = i.jiebao()
            if t[2] == c:
                continue
            ans.append([t[0], t[2]])
            c = t[2]
        return ans




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