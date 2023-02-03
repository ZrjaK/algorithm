def lengthOfLIS(nums):
    h = []
    for i in nums:
        t = bisect_left(h, i)
        if t < len(h):
            h[t] = i
        else:
            h.append(i)
    return len(h)