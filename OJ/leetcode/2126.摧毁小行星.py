# 题目：2126.摧毁小行星
# 难度：MEDIUM
# 最后提交：2022-04-08 11:45:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids:
            if mass < asteroids[-1]:
                return False
            mass += asteroids.pop()
        return True