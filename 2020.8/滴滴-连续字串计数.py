n = int(input().strip())
map = []
for _ in range(n):
    map.append([ch for ch in input().strip()])


def findallC():
    for i in range(n):
        for j in range(n):
            if map[i][j] == 'C':
                yield i, j


def ok(i: int, j: int, okChar: str) -> bool:
    if 0 <= i < n and 0 <= j < n:
        return map[i][j] == okChar
    return False


resultCount = 0


def nextCh(nowCh: str):
    return 'CHINA'['CHINA'.index(nowCh) - 4]


visited = set()


def dfs(x: int, y: int):
    if (x, y) in visited:
        return
    global resultCount
    if map[x][y] == 'A':
        resultCount += 1
        return
    visited.add((x, y))
    directions = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    for direc in directions:
        if ok(direc[0], direc[1], nextCh(map[x][y])):
            dfs(*direc)


for cI, cJ in findallC():
    visited = set()
    dfs(cI, cJ)
print(resultCount)
