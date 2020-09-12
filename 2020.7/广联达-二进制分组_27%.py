import sys
from collections import defaultdict


def getRoots():
    for i, (r, c) in enumerate(zip(rudu, chudu)):
        if c != 0 and r == 0:
            yield i


def dfs(rootIndex):
    if rootIndex in dfsVisited:
        return
    dfsVisited.add(rootIndex)
    if rootIndex in edges:
        for nextNodeIndex in edges[rootIndex]:
            dfs(nextNodeIndex)


n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))[:n]
rudu, chudu = [0] * len(arr), [0] * len(arr)
edges = defaultdict(list)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] & arr[j] == arr[i]:
            edges[j].append(i)
            chudu[j] += 1
            rudu[i] += 1
        elif arr[i] & arr[j] == arr[j]:
            edges[i].append(j)
            chudu[i] += 1
            rudu[j] += 1

dfsVisited = set()
ans = 0
for root in getRoots():
    dfs(root)
    ans += 1
singleNodes = set(range(len(arr))).difference(dfsVisited)
for single in singleNodes:
    potential = [single ^ (1 << b) for b in range(m)]
    found = False
    for po in potential:
        for x in arr:
            if po % x == po or po % x == x:
                found = True
                break
        if found:
            break
    if not found:
        ans += 1
sys.stdout.write(str(ans))
