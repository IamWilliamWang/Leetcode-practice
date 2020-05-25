import sys

if __name__ == '__main__':
    # 读取第一行的n,m,q
    values = list(map(int, sys.stdin.readline().strip().split()))
    [rows, cols, ask_times] = values  # 行数，列数，询问次数
    # 读取原始矩阵
    matrix = []
    for i in range(rows):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        matrix += [values]
    # 先处理各行
    for row in range(rows):  # 每行遍历填补
        zeroNumberIndex = []
        nonZeroNumberIndex = []
        # 统计零、非零的位置
        for col in range(cols):
            if matrix[row][col] == 0:
                zeroNumberIndex += [col]
            else:
                nonZeroNumberIndex += [col]
        if len(nonZeroNumberIndex) <= 1:  # 如果一行只有一个非0，这行就管不了了
            continue
        step = int((matrix[row][nonZeroNumberIndex[1]] - matrix[row][nonZeroNumberIndex[0]]) / (
                nonZeroNumberIndex[1] - nonZeroNumberIndex[0]))  # 求等差
        for index in zeroNumberIndex:  # 根据求出来的等差填补所有的零
            matrix[row][index] = int(matrix[row][index - 1] + step)
    # 然后处理各列
    for col in range(cols):
        zeroNumberIndex = []
        nonZeroNumberIndex = []
        # 统计零的位置
        for row in range(rows):
            if matrix[row][col] == 0:
                zeroNumberIndex += [row]
            else:
                nonZeroNumberIndex += [row]
        if len(nonZeroNumberIndex) <= 1:  # 如果一列只有一个非0，这行就管不了了
            continue
        step = int((matrix[nonZeroNumberIndex[1]][col] - matrix[nonZeroNumberIndex[0]][col]) / (
                nonZeroNumberIndex[1] - nonZeroNumberIndex[0]))  # 求等差
        for index in zeroNumberIndex:  # 根据求出来的等差填补所有的零
            matrix[index][col] = int(matrix[index - 1][col] + step)
    # 为了防止处理完列后，有些不能处理的行现在又活了，所以再遍历一遍各行
    for row in range(rows):  # 每行遍历填补
        zeroNumberIndex = []
        nonZeroNumberIndex = []
        # 统计零、非零的位置
        for col in range(cols):
            if matrix[row][col] == 0:
                zeroNumberIndex += [col]
            else:
                nonZeroNumberIndex += [col]
        if len(nonZeroNumberIndex) <= 1:  # 如果一行只有一个非0，这行就管不了了
            continue
        step = int((matrix[row][nonZeroNumberIndex[1]] - matrix[row][nonZeroNumberIndex[0]]) / (
                nonZeroNumberIndex[1] - nonZeroNumberIndex[0]))  # 求等差
        for index in zeroNumberIndex:  # 根据求出来的等差填补所有的零
            matrix[row][index] = int(matrix[row][index - 1] + step)
    # 询问并输出结果
    for ask in range(ask_times):
        values = list(map(int, sys.stdin.readline().strip().split()))
        [row, col] = values
        print(matrix[row - 1][col - 1] if matrix[row - 1][col - 1] is not 0 else 'Unknown')
