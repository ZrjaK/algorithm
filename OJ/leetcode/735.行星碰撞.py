# 题目：735.行星碰撞
# 难度：MEDIUM
# 最后提交：2022-04-14 13:11:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans