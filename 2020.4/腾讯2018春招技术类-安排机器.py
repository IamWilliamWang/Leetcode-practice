import sys

# 输入
machineCount, missionCount = list(map(int, sys.stdin.readline().strip().split()))
machineInfo = []
for _ in range(machineCount):
    maxWorkTime, machineLevel = list(map(int, sys.stdin.readline().strip().split()))
    machineInfo += [(machineLevel, maxWorkTime)]
machineInfo.sort()
missionInfo = []
for _ in range(missionCount):
    missionTime, missionLevel = list(map(int, sys.stdin.readline().strip().split()))
    missionInfo += [(missionLevel, missionTime)]
# 处理
result = 0
resultCount = 0
machineBusy = [False] * machineCount
for mission in missionInfo:
    missionLevel, missionTime = mission
    for machineId in range(machineCount):
        if not machineBusy[machineId] and machineInfo[machineId][0] >= missionLevel and machineInfo[machineId][1] >= missionTime:
            machineBusy[machineId] = True
            resultCount += 1
            result += 200 * missionTime + 3 * missionLevel
print(resultCount, result)
