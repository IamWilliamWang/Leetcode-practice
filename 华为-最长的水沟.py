def main():
    rows, cols = list(map(int, input().strip().split()))
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().strip().split())))
    if not rows or not cols:
        print(0)
        return
    edges = {(i, j): [] for i in range(rows) for j in range(cols)}
    degrees = {(i, j): 0 for i in range(rows) for j in range(cols)}  # 入度
    for x in range(rows):
        for y in range(cols):
            for toX, toY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not 0 <= toX < rows or not 0 <= toY < cols:
                    continue
                if matrix[toX][toY] < matrix[x][y]:
                    edges[(x, y)].append((toX, toY))  # 指向
                    degrees[(toX, toY)] += 1  # 入度+1

    round = 0  # 多少轮拓扑排序
    visitedXY = set()  # 访问过到坐标
    while len(visitedXY) < rows * cols:  # 直到所有都被访问
        removedXList, removedYList = [], []
        for x, y in degrees:
            if (x, y) in visitedXY:  # 失效到坐标不要管
                continue
            if degrees[x, y] == 0:  # 保存入度是0的所有坐标
                removedXList += [x]
                removedYList += [y]
        for x, y in zip(removedXList, removedYList):  # 所有指向的节点的入度-1
            for tarX, tarY in edges[x, y]:
                degrees[tarX, tarY] -= 1  # 入度-1
            visitedXY.add((x, y))
        round += 1
    print(round)


main()
