from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        x, y = 0, 0
        restCount = len(matrix) * len(matrix[0])
        clockwiseTraversal = []
        while restCount and left <= right and top <= bottom:
            while restCount and y <= right:
                clockwiseTraversal.append(matrix[x][y])
                restCount -= 1
                if y == right:
                    break
                y += 1
            top += 1
            x += 1
            while restCount and x <= bottom:
                clockwiseTraversal.append(matrix[x][y])
                restCount -= 1
                if x == bottom:
                    break
                x += 1
            right -= 1
            y -= 1
            while restCount and y >= left:
                clockwiseTraversal.append(matrix[x][y])
                restCount -= 1
                if y == left:
                    break
                y -= 1
            bottom -= 1
            x -= 1
            while restCount and x >= top:
                clockwiseTraversal.append(matrix[x][y])
                restCount -= 1
                if x == top:
                    break
                x -= 1
            left += 1
            y += 1
        return clockwiseTraversal


print(Solution().spiralOrder([[1, 2, 3]]))
