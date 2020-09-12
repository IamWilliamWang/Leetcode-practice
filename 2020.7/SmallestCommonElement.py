from typing import List
import numpy as np
from collections import Counter


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mat = np.array(mat)
        if not all(mat.shape): return -1
        heap = mat.reshape(-1, mat.size).squeeze().tolist()
        okSet = {key for key, count in Counter(heap).items() if count == len(mat)}
        return min(okSet) if okSet else -1


print(Solution().smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
