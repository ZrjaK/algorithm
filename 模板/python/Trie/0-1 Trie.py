class Trie:
    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0
    
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
            node.cnt += 1
            
    def erase(self, x):
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
            node.cnt -= 1
    
    # 树中元素 ^ x > lo的数量
    def query(self, x, lo):
        res = 0
        node = self
        for i in range(31, -1, -1):
            if lo>>i & 1 == 0:
                if x>>i & 1:
                    if node.left:
                        res += node.left.cnt
                    if node.right:
                        node = node.right
                    else:
                        return res
                else:
                    if node.right:
                        res += node.right.cnt
                    if node.left:
                        node = node.left
                    else:
                        return res
            else:
                if x>>i & 1:
                    if node.left:
                        node = node.left
                    else:
                        return res
                else:
                    if node.right:
                        node = node.right
                    else:
                        return res
        return res

            
    def getMaxXor(self, x):
        res = 0
        node = self
        for i in range(31, -1, -1):
            f = False
            if x>>i & 1:
                if node.left and node.left.cnt:
                    f = True
                    node = node.left
                elif node.right.cnt:
                    node = node.right
            else:
                if node.right and node.right.cnt:
                    f = True
                    node = node.right
                elif node.left.cnt:
                    node = node.left
            if f:
                res |= 1<<i
        return res