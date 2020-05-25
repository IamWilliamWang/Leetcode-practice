class Solution:
    def rotate(self, matrix) -> None:
        if not matrix:
            return
        row_count = len(matrix)
        # 沿着水平中轴线垂直旋转
        for row_index in range(row_count // 2):
            matrix[row_index], matrix[row_count - 1 - row_index] = matrix[row_count - 1 - row_index], matrix[row_index]
        # 沿着左上右下对角线旋转
        for row_index in range(row_count):
            for col_index in range(row_index):
                matrix[row_index][col_index], matrix[col_index][row_index] = matrix[col_index][row_index], matrix[row_index][col_index]
        print(matrix)

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
Solution().rotate(matrix)
