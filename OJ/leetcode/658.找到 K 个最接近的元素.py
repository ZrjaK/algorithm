# 题目：658.找到 K 个最接近的元素
# 难度：MEDIUM
# 最后提交：2022-04-20 13:52:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = bisect_left(arr, x)
        res = deque()
        l = i-1
        r = i
        while k > 0:
            if l >= 0 and r < len(arr):
                if x-arr[l] < arr[r]-x or (x-arr[l] == arr[r]-x and arr[l]<arr[r]):
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
                k -= 1
            elif l >= 0:
                res.appendleft(arr[l])
                l -= 1
                k -= 1
            elif r < len(arr):
                res.append(arr[r])
                r += 1
                k -= 1
            else:
                return res
        return list(res)
                