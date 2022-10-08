# 题目：1577.数的平方等于两数乘积的方法数
# 难度：MEDIUM
# 最后提交：2022-06-10 16:00:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getTriplets(map1: Counter, map2: Counter):
            triplets = 0
            for num1, count1 in map1.items():
                square = num1 * num1
                for num2, count2 in map2.items():
                    if square % num2 == 0:
                        num3 = square // num2
                        if num2 == num3:
                            curTriplets = count1 * count2 * (count2 - 1) // 2
                            triplets += curTriplets
                        elif num2 < num3 and num3 in map2:
                            count3 = map2[num3]
                            curTriplets = count1 * count2 * count3
                            triplets += curTriplets
            return triplets

        map1 = collections.Counter(nums1)
        map2 = collections.Counter(nums2)
        return getTriplets(map1, map2) + getTriplets(map2, map1)
