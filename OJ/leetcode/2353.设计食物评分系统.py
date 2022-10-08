# 题目：2353.设计食物评分系统
# 难度：MEDIUM
# 最后提交：2022-07-24 10:49:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d = defaultdict(int)
        for f, r in zip(foods, ratings):
            self.d[f] = r
        self.f = defaultdict(str)
        self.c1 = defaultdict(SortedSet)
        for f, c in zip(foods, cuisines):
            self.c1[c].add((-self.d[f], f))
            self.f[f] = c
        
        


    def changeRating(self, food: str, newRating: int) -> None:
        c = self.f[food]
        self.c1[c].remove((-self.d[food], food))
        self.d[food] = newRating
        self.c1[c].add((-self.d[food], food))

    def highestRated(self, cuisine: str) -> str:
        return self.c1[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)