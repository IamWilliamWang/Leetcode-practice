from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[right] > numbers[mid]:
                right = mid - 1
            elif numbers[right] < numbers[mid]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]


print(Solution().minArray([2, 2, 2, 0, 1]))
