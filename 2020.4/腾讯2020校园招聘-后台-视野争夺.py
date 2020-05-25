import sys
import numpy as np


def minus(nowRiverSpace: np.ndarray, choiceEye: list) -> np.ndarray:
    nowRiverSpace = nowRiverSpace.copy()
    nowRiverSpace[choiceEye[0]:(choiceEye[1] + 1 if choiceEye[1] <= riverWidth else riverWidth + 1)] = 1
    return nowRiverSpace


def dp(restEyes: list, nowRiverSpace: np.ndarray) -> int:
    if not restEyes:
        return -1
    if np.all(nowRiverSpace):
        return 0
    potentialResult = []
    for choiceEye in restEyes:
        next = restEyes.copy()
        next.remove(choiceEye)
        ans = dp(next, minus(nowRiverSpace, choiceEye))
        if ans != -1:
            potentialResult += [1 + ans]
    return min(potentialResult) if potentialResult != [] else -1


eyesCount, riverWidth = list(map(int, sys.stdin.readline().strip().split()))  # 守卫数量和河道宽度
eyes = []  # 保存所有真视守卫的范围
for _ in range(eyesCount):  # 逐个输入
    eyes.append(tuple(map(int, sys.stdin.readline().strip().split())))
riverSpace = [0] * (riverWidth + 1)
print(dp(eyes, np.array(riverSpace)))
