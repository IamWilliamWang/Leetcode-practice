from itertools import combinations

rows, cols, seleRows, seleCols = list(map(int, input().strip().split()))
coinMap = []
for _ in range(rows):
    coinMap.append(list(map(int, input().strip().split())))


def sumDistance(map: list):
    visited = set()
    queue = [(0, 0)]
    result = 0
    rows, cols = len(map), len(map[0])
    while queue:
        i, j = queue.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for dir in [(i, j + 1), (i + 1, j)]:
            if 0 <= dir[0] < rows and 0 <= dir[1] < cols and (dir[0], dir[1]) not in visited:
                queue.append(dir)
                result += abs(map[dir[0]][dir[1]] - map[i][j])
    return result


minResult = 2 ** 31 - 1
for rowRange, colRange in ((rowRange, colRange) for rowRange in combinations(range(rows), seleRows) for colRange in
                           combinations(range(cols), seleCols)):
    subMat = [[coinMap[x][y] for y in colRange] for x in rowRange]
    minResult = min(minResult, sumDistance(subMat))
print(minResult)
