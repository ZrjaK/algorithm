class Trie:
    def __init__(self):
        self.left = None
        self.right = None
    
    def insert(self, x):
        node = self
        for i in range(31, -1, -1):
            if x>>i & 1:
                if not node.right:
                    node.right = Trie()
                node = node.right
            else:
                if not node.left:
                    node.left = Trie()
                node = node.left
            
    def getMaxXor(self, x):
        res = 0
        node = self
        for i in range(31, -1, -1):
            f = False
            if x>>i & 1:
                if node.left:
                    f = True
                    node = node.left
                else:
                    node = node.right
            else:
                if node.right:
                    f = True
                    node = node.right
                else:
                    node = node.left
            if f:
                res |= 1<<i
        return res