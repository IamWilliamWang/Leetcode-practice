array = [[1, 4, 6, 8, 10, 12, 13],
         [3, 5, 7, 8, 11, 13, 14],
         [5, 6, 7, 9, 13, 15, 16],
         [6, 9, 11, 12, 13, 16, 17]]


class Solution:
    def GetNum(self, i, j):
        rows = len(self.array)
        cols = len(self.array[0])
        if i < 0 or j < 0:
            return -65535
        if i >= rows or j >= cols:
            return -65535
        return self.array[i][j]

    def Closest2Target(self, values):
        values = [self.target - value if value <= self.target else 65535 for value in values]
        return values.index(min(values))

    def NextStep(self, now_x, now_y):
        neighbour = []
        neighbour += [self.GetNum(now_x + 1, now_y)]
        neighbour += [self.GetNum(now_x - 1, now_y)]
        neighbour += [self.GetNum(now_x, now_y + 1)]
        neighbour += [self.GetNum(now_x, now_y - 1)]
        if not neighbour:
            return -1, -1
        best_index = self.Closest2Target(neighbour)
        if best_index is 0:
            return now_x + 1, now_y
        if best_index is 1:
            return now_x - 1, now_y
        if best_index is 2:
            return now_x, now_y + 1
        return now_x, now_y - 1

    # array 二维列表
    def Find(self, target, array):
        self.target = target
        self.array = array
        pointer_x = 0
        pointer_y = 0
        while True:
            pointer_x, pointer_y = self.NextStep(pointer_x, pointer_y)
            if pointer_x is -1 or pointer_y is -1:
                print('没有搜到')
                return False
            if self.array[pointer_x][pointer_y] is target:
                print('%d已找到，坐标(%d, %d)' % (self.target, pointer_x, pointer_y))
                return True


Solution().Find(14, array)
