# 题目：1912.设计电影租借系统
# 难度：HARD
# 最后提交：2022-09-22 15:43:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        from sortedcontainers import SortedSet
        self.s = defaultdict(SortedSet)
        self.d = defaultdict(int)
        for shop, movie, price in entries:
            self.s[movie].add((price, shop))
            self.d[movie, shop] = price
        self.r = SortedSet()


    def search(self, movie: int) -> List[int]:
        return [i[1] for i in self.s[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.s[movie].remove((self.d[movie, shop], shop))
        self.r.add((self.d[movie, shop], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.r.remove((self.d[movie, shop], shop, movie))
        self.s[movie].add((self.d[movie, shop], shop))

    def report(self) -> List[List[int]]:
        return [i[1:] for i in self.r[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()