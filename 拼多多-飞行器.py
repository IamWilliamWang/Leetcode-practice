def printResult(distance, dotArray):
    backwardCount = 0
    for dot in dotArray:
        distance -= dot
        if distance == 0:
            print('paradox', end='')
            break
        elif distance < 0:
            backwardCount += 1
            distance = -distance
    else:
        print(distance, backwardCount, end='')


distance, N = list(map(int, input().strip().split()))
dotArray = list(map(int, input().strip().split()))[:N]
printResult(distance, dotArray)
# printResult(10, [6, 3])  # 1 0
# printResult(10, [6, 3, 3, 3])  # 1 2
# printResult(6, [4, 2, 6])  # paradox
