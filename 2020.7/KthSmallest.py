from typing import List
import sys
sys.path.append('./2020.5')
from MergeKLists import MergeSort


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k > len(matrix) * len(matrix[0]):
            return 0
        return MergeSort(matrix).sort(True)[k - 1]


print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
