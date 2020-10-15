def main():
    stepCount = int(input().strip())  # 试了多少步
    x, y = 0, 0
    goodLocation = {(x, y)}  # 可以踩的坐标
    for _ in range(stepCount):
        direction, success = list(map(int, input().strip().split()))  # 方向，是否成功
        if success != 1:  # 不成功就不管了
            continue
        if direction == 0:  # 上
            x -= 1
        elif direction == 1:  # 下
            x += 1
        elif direction == 2:  # 左
            y -= 1
        elif direction == 3:  # 右
            y += 1
        goodLocation.add((x, y))  # 这个坐标可以踩
    goalX, goalY = x, y  # 终点的x和y
    bfs = [(0, 0, 0)]  # x、y、已经走了多少步
    visited = set()
    while bfs:
        x, y, step = bfs.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == (goalX, goalY):  # 第一次到达重点，一定是最短的
            return step
        bfs += [(i, j, step + 1) for i, j in ((x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)) if (i, j) in goodLocation]


for _ in range(int(input().strip())):
    print(main())
