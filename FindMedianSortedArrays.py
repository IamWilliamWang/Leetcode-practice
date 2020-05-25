from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        centerIndex = (len(nums1) + len(nums2)) // 2
        p1, p2 = 0, 0  # 储存的是下一次要访问的位置
        combinedList = []  # 合并好的列表
        # 不停的搜索，直到两个指针有越界的或者找到了中点位置
        while p1 < len(nums1) and p2 < len(nums2) and p1 + p2 < centerIndex:
            if nums1[p1] <= nums2[p2]:
                combinedList.append(nums1[p1])
                p1 += 1
            else:
                combinedList.append(nums2[p2])
                p2 += 1
        # 如果p1越界了，把p2挪到正确的位置，并且把之前的元素都加进来
        if p1 == len(nums1):
            combinedList += nums2[p2:centerIndex - p1]
            p2 = centerIndex - p1
        elif p2 == len(nums2):
            combinedList += nums1[p1:centerIndex - p2]
            p1 = centerIndex - p2
        # 计算结果：当为奇数时，p1或者p2指向的是中位数
        if (len(nums1) + len(nums2)) % 2 == 1:
            if p1 < len(nums1) and p2 < len(nums2):  # 当指针都没有越界时
                return min(nums1[p1], nums2[p2]) * 1.0
            if p1 == len(nums1):
                return nums2[p2]
            if p2 == len(nums2):
                return nums1[p1]
            return 0.0
        else:  # 为偶数时，中间的左边位置已经访问过了
            if p1 < len(nums1) and p2 < len(nums2):
                return (min(nums1[p1], nums2[p2]) + combinedList[-1]) / 2
            if p1 == len(nums1):
                return (nums2[p2] + combinedList[-1]) / 2
            if p2 == len(nums2):
                return (nums1[p1] + combinedList[-1]) / 2


print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
