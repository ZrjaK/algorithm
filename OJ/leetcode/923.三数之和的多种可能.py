# 题目：923.三数之和的多种可能
# 难度：MEDIUM
# 最后提交：2022-06-06 19:32:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = Counter(arr)
        arr = sorted(list(set(arr)))
        ans = 0
        for i in range(len(arr)):
            l, r = i, len(arr)-1
            while l <= r:
                s = arr[i] + arr[l] + arr[r]
                if s == target:
                    if arr[i] == arr[l] == arr[r]:
                        t = c[arr[i]]
                        ans += t * (t-1) * (t-2) // 6
                        break
                    elif arr[i] != arr[l] and arr[l] != arr[r]:
                        ans += c[arr[i]] * c[arr[l]] * c[arr[r]]
                        l += 1
                        r -= 1
                    else:
                        ans += c[arr[i]] * (c[arr[l]]-1) * c[arr[r]] // 2
                        l += 1
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return ans % int(1e9+7)
