class STNode:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy

class SegmentTree:
    def __init__(self):
        self.root = STNode()
    
    def add(self, node, l, r, start, end, x):
        if l == start and r == end:
            node.lazy += x
            return
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            self.add(node.left, l, mid, start, end, x)
        elif start > mid:
            self.add(node.right, mid+1, r, start, end, x)
        else:
            self.add(node.left, l, mid, start, mid, x)
            self.add(node.right, mid+1, r, mid+1, end, x)
        self.pushup(node, mid-l+1, r-mid)

    def query(self, node, l, r, start, end):
        if l == start and r == end:
            return node.lazy * (r-l+1) + node.val
        mid = l+r>>1
        self.pushdown(node)
        if end <= mid:
            res = self.query(node.left, l, mid, start, end)
        elif start > mid:
            res = self.query(node.right, mid+1, r, start, end)
        else:
            res = self.query(node.left, l, mid, start, mid) + \
                self.query(node.right, mid+1, r, mid+1, end)
        self.pushup(node, mid-l+1, r-mid)
        return res
    
    def pushdown(self, node):
        if not node.left:
            node.left = STNode()
        if not node.right:
            node.right = STNode()
        if node.lazy:
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0
    
    def pushup(self, node, ln, rn):
        node.val = node.left.val + node.right.val + node.left.lazy * ln + node.right.lazy * rn
