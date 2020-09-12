from heapq import heappop, heappush


def ok(i: int, j: int):
    return 0 <= i < rows and 0 <= j < cols


def BFS(startX: int, startY: int):
    global resultCost
    queue = [(costMap[startX][startY], startX, startY)]  # 到达此点后累计的cost, x,y
    visited = set()
    while queue:
        cost, i, j = heappop(queue)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == rows - 1:
            resultCost = min(resultCost, cost)
        nexts = [(cost + costMap[dir[0]][dir[1]], dir[0], dir[1]) for dir in [(i + 1, j), (i, j + 1), (i, j - 1)] if
                 ok(*dir) and (dir[0], dir[1]) not in visited]
        for tmp in nexts:
            heappush(queue, tmp)


rows, cols = list(map(int, input().strip().split()))
costMap = []
for _ in range(rows):
    costMap.append(list(map(int, input().strip().split())))

resultCost = 2 ** 31 - 1
BFS(0, costMap[0].index(min(costMap[0])))
print(resultCost)
