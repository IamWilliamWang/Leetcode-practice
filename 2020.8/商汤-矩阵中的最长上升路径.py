def ok(i: int, j: int, biggerThan: int) -> bool:
    if 0 <= i < rows and 0 <= j < cols:
        if (i, j) in visited:
            return False
        if matrix[i][j] <= biggerThan:
            return False
        return True
    return False


def getNextXY(i: int, j: int):
    directions = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
    return [di for di in directions if ok(di[0], di[1], matrix[i][j])]


def dfs(i: int, j: int, pathLen: int):
    global result
    visited.add((i, j))
    nextXY = getNextXY(i, j)
    if not nextXY:
        result = max(result, pathLen)
        return
    for x, y in nextXY:
        dfs(x, y, pathLen + 1)


rows, cols = list(map(int, input().strip().split()))
matrix = []
minI, minJ, minNum = -1, -1, 2 ** 31 - 1
for _ in range(rows):
    matrix.append(list(map(int, input().strip().split())))
    if min(matrix[-1]) < minNum:
        minNum = min(matrix[-1])
        minI = len(matrix) - 1
        minJ = matrix[-1].index(minNum)
visited = set()
result = 0
dfs(minI, minJ, 1)
print(result)
