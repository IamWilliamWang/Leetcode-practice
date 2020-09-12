from test_script import speedtest

from itertools import chain


def getResult(lunch, dinner, minTastyValue):
    if minTastyValue == 0:
        return 0
    lunch.sort(key=lambda x: (-x[1], x[0]))
    dinner.sort(key=lambda x: (-x[1], x[0]))
    minCal = 2 ** 31 - 1
    for food in chain(lunch, dinner):
        if food[1] >= minTastyValue:
            minCal = min(minCal, food[0])
    for i in range(len(lunch)):
        for j in range(len(dinner)):
            if lunch[i][1] + dinner[j][1] >= minTastyValue:
                minCal = min(minCal, lunch[i][0] + dinner[j][0])
    return minCal if minCal != 2 ** 31 - 1 else -1


lunchCount, dinnerCount, minTastyValue = list(map(int, input().strip().split()))
lunch = []  # 热量，美味值
dinner = []
for _ in range(lunchCount):
    lunch.append(tuple(map(int, input().strip().split())))
for _ in range(dinnerCount):
    dinner.append(tuple(map(int, input().strip().split())))
print(getResult(lunch, dinner, minTastyValue))

# speedtest((getResult, lambda *args: 4), ([[9, 1], [4, 9], [3, 1], [2, 3], [6, 5]], [[9, 8]], 9))
# speedtest((getResult, lambda *args: 0), ([[3, 1]], [[2, 1]], 0))
# speedtest((getResult, lambda *args: 5), ([[1, 1], [2, 5], [3, 7]], [[2, 4], [4, 8], [6, 9]], 10))
# speedtest((getResult, lambda *args: -1), ([[3, 1], [2, 1]], [[1, 2]], 4))
