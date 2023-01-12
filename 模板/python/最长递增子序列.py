class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        h = []
        for i in nums:
            t = bisect_left(h, i)
            if t < len(h):
                h[t] = i
            else:
                h.append(i)
        return len(h)