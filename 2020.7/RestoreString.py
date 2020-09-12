from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newArray = [''] * len(s)
        for i, indices in enumerate(indices):
            newArray[indices] = s[i]
        return ''.join(newArray)
