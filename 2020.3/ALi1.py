import sys
import math

if __name__ == '__main__':
    # 读取第一行的n
    cols = int(sys.stdin.readline().strip())
    matrix = []
    for row in range(3):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        matrix += [values]
    best_lists = []
    for row in range(3):
        now_number = matrix[row][0]
        list = [now_number]
        for col in range(1, cols):
            minValue = 65535
            minIndex = -1
            for searching_row in range(3):
                if int(math.fabs(matrix[searching_row][col] - now_number)) < minValue:
                    minValue = int(math.fabs(matrix[searching_row][col] - now_number))
                    minIndex = searching_row
            now_number = matrix[minIndex][col]
            list += [now_number]
        best_lists += [list]
    minResult = 65535
    for list in best_lists:
        result = 0
        for i in range(1, len(list)):
            result += int(math.fabs(list[i] - list[i - 1]))
        if result < minResult:
            minResult = result
    print(minResult)
