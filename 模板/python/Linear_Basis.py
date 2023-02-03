logN = 64
class Linear_Basis:
    def __init__(self) -> None:
        self.b = [0] * logN
        self.d = []
        self.zero = 0
        self.hasrebuild = False

    def insert(self, x):
        self.hasrebuild = False
        for i in range(logN - 1, -1, -1):
            if x >> i & 1:
                if not self.b[i]:
                    self.b[i] = x
                    return True
                else:
                    x ^= self.b[i]
        if x == 0:
            self.zero = 1
        return False
    
    # x 与线性基异或的最大值，x=0 时表示线性基能表示出的最大值
    def qrymx(self, x=0):
        for i in range(logN - 1, -1, -1):
            x = max(x, x ^ self.b[i])
        return x
    
    def qrymn(self):
        for i in range(logN):
            if self.b[i]:
                return self.b[i]

    def join(self, t):
        for i in range(logN-1, -1, -1):
            self.insert(t.b[i])

    def rebuild(self):
        self.hasrebuild = True
        self.d = []
        for i in range(logN - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if self.b[i] >> j & 1:
                    self.b[i] ^= self.b[j]
        for i in range(logN):
            if self.b[i]:
                self.d.append(self.b[i])

    # rebuild before kth
    def kth(self, k):
        if not self.hasrebuild:
            self.rebuild()
        k -= self.zero
        if k >= 1 << len(self.d):
            return -1
        ans = 0
        for i in range(logN - 1, -1, -1):
            if k >> i & 1:
                ans ^= self.d[i]
        return ans
    
    def rank(self, x):
        if not self.hasrebuild:
            self.rebuild()
        ans = 0
        for i in range(len(self.d) - 1, -1, -1):
            if x >= self.d[i]:
                ans += 1 << i
                x ^= self.d[i]
        return ans + self.zero