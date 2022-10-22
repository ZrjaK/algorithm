class SegmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0] + nums
        self.val = [0] * 4*n
        self.lazy = [0] * 4*n
        self.buildTree(1, 1, n)
    
    def buildTree(self, k, l, r):
        if l == r:
            self.val[k] = self.nums[l]
            return
        mid = l+r>>1
        self.buildTree(2*k, l, mid)
        self.buildTree(2*k+1, mid+1, r)
        self.val[k] = self.val[2*k] + self.val[2*k+1]
    
    def add(self, k, l, r, start, end, x):
        if l == start and r == end:
            self.lazy[k] += x
            return
        self.val[k] += (end-start+1) * x
        mid = l+r>>1
        if end <= mid:
            self.add(2*k, l, mid, start, end, x)
        elif start > mid:
            self.add(2*k+1, mid+1, r, start, end, x)
        else:
            self.add(2*k, l, mid, start, mid, x)
            self.add(2*k+1, mid+1, r, mid+1, end, x)
        

    def query(self,k,l,r,start,end,p):
        p += self.lazy[k]
        if l == start and r == end:
            return p * (end-start+1) + self.val[k]
        mid = l+r>>1
        if end <= mid:
            return self.query(2*k, l, mid, start, end, p)
        elif start > mid:
            return self.query(2*k+1, mid+1, r, start, end, p)
        return self.query(2*k, l, mid, start, mid, p) + self.query(2*k+1, mid+1, r, mid+1, end, p)
