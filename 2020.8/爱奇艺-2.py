def nextXY(ch: str):
    if ch == 'N':
        nextStep = (visited[-1][0] - 1, visited[-1][1])
    elif ch == 'S':
        nextStep = (visited[-1][0] + 1, visited[-1][1])
    elif ch == 'E':
        nextStep = (visited[-1][0], visited[-1][1] + 1)
    elif ch == 'W':
        nextStep = (visited[-1][0], visited[-1][1] - 1)
    else:
        raise ValueError
    if nextStep in visited:
        return None
    return nextStep


path = input().strip()
visited = [(0, 0)]
for selection in path:
    nextStep = nextXY(selection)
    if not nextStep:
        print('True')
        exit(0)
    visited.append(nextStep)
print('False')
