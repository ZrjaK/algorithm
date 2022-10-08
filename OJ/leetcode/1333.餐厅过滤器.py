# 题目：1333.餐厅过滤器
# 难度：MEDIUM
# 最后提交：2022-08-30 15:25:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        h = []
        for i in restaurants:
            if i[2] >= veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance:
                h.append(i)
        h.sort(key=lambda x:(-x[1], -x[0]))
        return [i[0] for i in h]