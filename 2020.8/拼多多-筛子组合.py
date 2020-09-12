from test_script import speedtest

from collections import defaultdict

def getResult(sieveArray: list):
    def idEquals(sieve1Id: tuple, sieve2Id: tuple) -> bool:
        j = -len(sieve2Id)
        while j < 0 and sieve2Id[j] != sieve1Id[0]:
            j += 1
        if j >= 0:  # 没找到说明有一个数字在对面
            return False
        for i in range(len(sieve1Id)):
            if sieve1Id[i] != sieve2Id[j]:
                return False
            j += 1
        return True

    sieveIds = []
    for up, down, left, right, front, back in sieveArray:  # 记录1周围的序列（逆时针）作为这个筛子的唯一标识
        if up == 1:
            sieveIds.append(tuple([left, front, right, back]))
        elif down == 1:
            sieveIds.append(tuple([right, front, left, back]))
        elif left == 1:
            sieveIds.append(tuple([down, front, up, back]))
        elif right == 1:
            sieveIds.append(tuple([up, front, down, back]))
        elif front == 1:
            sieveIds.append(tuple([left, down, right, up]))
        elif back == 1:
            sieveIds.append(tuple([right, down, left, up]))
    sieveClassesCounter = defaultdict(int)
    for sieveId in sieveIds:
        for existsSieveId in sieveClassesCounter:
            if idEquals(sieveId, existsSieveId):
                sieveClassesCounter[existsSieveId] += 1
                break
        else:
            sieveClassesCounter[sieveId] = 1
    return sorted(sieveClassesCounter.values(), reverse=True)


N = int(input().strip())
sieveArray = []
for _ in range(N):
    sieveArray.append(tuple(map(int, input().strip().split())))
result = getResult(sieveArray)
print(len(result))
print(' '.join(map(str, result)))

speedtest((getResult, lambda *args: [2]), [[[1, 2, 3, 4, 5, 6], [1, 2, 6, 5, 3, 4]]])
speedtest((getResult, lambda *args: [2, 1]), [[[1, 2, 3, 4, 5, 6], [1, 2, 6, 5, 3, 4], [1, 2, 3, 4, 6, 5]]])
speedtest((getResult, lambda *args: [2, 1, 1, 1, 1, 1, 1, 1, 1]), [[[2, 5, 1, 3, 4, 6],
                                                                    [5, 4, 3, 2, 1, 6],
                                                                    [1, 4, 6, 2, 3, 5],
                                                                    [1, 5, 6, 3, 4, 2],
                                                                    [6, 4, 2, 1, 5, 3],
                                                                    [3, 6, 4, 5, 2, 1],
                                                                    [1, 6, 3, 4, 2, 5],
                                                                    [5, 1, 4, 2, 6, 3],
                                                                    [6, 2, 3, 1, 5, 4],
                                                                    [5, 3, 6, 1, 4, 2]]])
