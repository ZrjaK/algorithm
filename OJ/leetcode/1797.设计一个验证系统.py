# 题目：1797.设计一个验证系统
# 难度：MEDIUM
# 最后提交：2023-02-09 20:09:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        from sortedcontainers import SortedList
        self.l = timeToLive
        self.d = {}
        self.sl = SortedList()

    def generate(self, tokenId: str, currentTime: int) -> None:
        while self.sl and self.sl[0] <= currentTime:
            self.sl.pop(0)
        if tokenId in self.d:
            self.sl.discard(self.d[tokenId])
        self.d[tokenId] = currentTime + self.l
        self.sl.add(currentTime + self.l)

    def renew(self, tokenId: str, currentTime: int) -> None:
        while self.sl and self.sl[0] <= currentTime:
            self.sl.pop(0)
        if tokenId not in self.d or self.d[tokenId] <= currentTime:
            return
        self.sl.discard(self.d[tokenId])
        self.d[tokenId] = currentTime + self.l
        self.sl.add(currentTime + self.l)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.sl and self.sl[0] <= currentTime:
            self.sl.pop(0)
        return len(self.sl)
        




# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)