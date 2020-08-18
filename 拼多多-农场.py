from functools import reduce


def getResult(_map, dfsX, dfsY):
    def getColor(i: int, j: int):
        if hasWall(i, j):
            return 0
        if 0 <= i < 6 and 0 <= j < 6:
            return _mapColor[i][j]
        return 0

    def canPaintColors(i: int, j: int):
        if hasWall(i, j):
            return set()
        cannot = {getColor(i - 1, j), getColor(i, j - 1), getColor(i + 1, j), getColor(i, j + 1)}
        return {1, 2, 3, 4, 5, 6}.difference(cannot)

    def hasWall(i: int, j: int):
        if not (0 <= i < 6 and 0 <= j < 6):
            return True
        return _map[i][j] == 0

    def dfs(i: int, j: int):
        if hasWall(i,j):
            return
        nonlocal ans
        global _mapVisited
        myColors = canPaintColors(i, j)
        _mapVisited[6 * i + j] = True
        if hasWall(i + 1, j) and hasWall(i, j + 1):
            ans += len(myColors)
        for color in myColors:
            _mapColor[i][j] = color
            dfs(i + 1, j)
            dfs(i, j + 1)
        _mapColor[i][j] = 0

    ans = 0
    _mapColor = [[0] * 6 for _ in range(6)]
    dfs(dfsX, dfsY)
    return ans


_map = []
_mapVisited = [False] * 36
for _ in range(6):
    _map += [list(map(int, input().strip().replace('#', '1').replace('*', '0')))]
answer = []
while not all(_mapVisited):
    for i, visit in enumerate(_mapVisited):
        if not visit:
            answer += [getResult(_map, i // 6, i - i // 6)]
print(reduce(lambda a, b: a * b, answer) % 1000000009, end='')
