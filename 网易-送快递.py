from collections import defaultdict
n, restBact = list(map(int, input().strip().split()))
adjDict = defaultdict(list)
for i, num in enumerate(list(map(int, input().strip().split()))):
    adjDict[i + 1] += [num]
    adjDict[num] += [i + 1]
path = [0]
resultPath = []


def dfs(nodeId: int, nowDepth):
    global maxDepth, resultPath
    pathSet, resultPathSet = set(path), set(resultPath)
    if nowDepth == restBact:
        if len(pathSet) > len(resultPathSet):
            resultPath = path.copy()
        return
    if len(pathSet) + restBact - nowDepth < len(resultPathSet):
        return
    for nextNodeId in adjDict[nodeId]:
        path.append(nextNodeId)
        dfs(nextNodeId, nowDepth + 1)
        path.pop()


dfs(0, 0)
print(len(set(resultPath)))
