from typing import List
import copy


def main():
    cols, rows = list(map(int, input().strip().split()))
    background = []
    for _ in range(rows):
        background.append([ch for ch in input().strip()])
    figureCols, figureRows = list(map(int, input().strip().split()))
    figure = []
    for _ in range(figureRows):
        figure.append([ch for ch in input().strip()])
    startI, startJ, colOffset, rowOffset = list(map(int, input().strip().split()))
    startI, startJ = startI - 1, startJ - 1  # 1-based -> 0-based index

    def paint(x: int, y: int):
        nowFrame = copy.deepcopy(background)
        for i in range(max(0, x), min(rows, x + figureRows)):  # i和j是操作点。要保证i和j的合理性
            for j in range(max(0, y), min(cols, y + figureCols)):
                nowFrame[i][j] = figure[i - x][j - y]  # i-x和j-y是人像的对应点
        return nowFrame

    def diff(frame1: List[List[str]], frame2: List[List[str]]):
        diffCount = 0
        for i in range(len(frame1)):
            for j in range(len(frame1[0])):
                if frame1[i][j] != frame2[i][j]:
                    diffCount += 1
        return diffCount

    result = 0
    lastFrame = background
    while True:
        frame = paint(startI, startJ)
        changePoints = diff(lastFrame, frame)
        if not changePoints:
            break
        result += changePoints
        lastFrame = frame
        # for row in frame:
        #     print(''.join(row))
        # print(result)
        startI += rowOffset
        startJ += colOffset
    return result


for _ in range(int(input().strip())):
    print(main())
