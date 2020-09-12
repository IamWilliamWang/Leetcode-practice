n = int(input().strip())
fi = [1, 1]
for _ in range(2, n ** 2):
    fi.append(fi[-2] + fi[-1])
result = [[0] * n for _ in range(n)]
i, j = 0, 0
leftBorder, rightBorder, topBorder, bottomBorder = 0, n - 1, 0, n - 1
while leftBorder <= rightBorder and topBorder <= bottomBorder:
    while fi and j < rightBorder:
        result[i][j] = fi.pop()
        j += 1
    topBorder += 1
    while fi and i < bottomBorder:
        result[i][j] = fi.pop()
        i += 1
    rightBorder -= 1
    while fi and j > leftBorder:
        result[i][j] = fi.pop()
        j -= 1
    bottomBorder -= 1
    while fi and i > topBorder:
        result[i][j] = fi.pop()
        i -= 1
    leftBorder += 1
if fi:
    result[i][j] = fi.pop()
for row in result:
    print(' '.join(map(str, row)))
