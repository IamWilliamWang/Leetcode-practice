from collections import defaultdict

maleIds = sorted(map(int, input().strip().split()))
femaleIds = sorted(map(int, input().strip().split()))
matches = defaultdict(list)
matchesCount = int(input().strip())
for _ in range(matchesCount):
    x, y = list(map(int, input().strip().split()))
    matches[x] += [y]
    matches[y] += [x]
selectedFemale = set()
result = 0


def dfs(maleI: int):
    global result
    if maleI == len(maleIds):
        result = max(result, len(selectedFemale))
        return
    maleId = maleIds[maleI]
    for target in matches[maleId]:
        if target not in selectedFemale:
            selectedFemale.add(target)
            dfs(maleI + 1)
            selectedFemale.remove(target)
        else:
            dfs(maleI + 1)


dfs(0)
print(result)
