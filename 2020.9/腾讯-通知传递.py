from collections import defaultdict
from test_script import GraphUtil

peopleCount, groupCount = list(map(int, input().strip().split()))
adjDict = defaultdict(set)
for _ in range(groupCount):
    line = list(map(int, input().strip().split()))
    assert len(line) == line[0] + 1
    line = line[1:]
    for i in range(len(line)):
        adjDict[line[i]].update(line[:i] + line[i + 1:])
result = 0
for _ in GraphUtil.DFS(adjDict, 0):
    result += 1
print(result)
