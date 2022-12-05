# 题目：2488.统计中位数为 K 的子数组
# 难度：HARD
# 最后提交：2022-11-27 12:41:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt = defaultdict(int)
        cnt[0] = 1  # i=pos 的时候 c 是 0，直接记到 cnt 中，这样下面不是大于就是小于
        c = 0
        for i in range(pos + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1

        ans = cnt[0] + cnt[1]  # i=pos 的时候 c 是 0，直接加到答案中，这样下面不是大于就是小于
        c = 0
        for i in range(pos - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt[c] + cnt[c + 1]
        return ans