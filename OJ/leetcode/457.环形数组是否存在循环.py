# 题目：457.环形数组是否存在循环
# 难度：MEDIUM
# 最后提交：2022-06-02 22:50:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(cur: int) -> int:
            return (cur + nums[cur]) % n  # 保证返回值在 [0,n) 中

        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow, fast = i, next(i)
            # 判断非零且方向相同
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False