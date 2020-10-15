import sys

sections = []
for line in sys.stdin:
    start, end = list(map(int, line.strip().split()))
    sections += [[start, end]]
sections.sort()
result = []
for i in range(1, len(sections)):
    if not result or result[-1][1] < sections[i][0]:
        result.append(sections[i])
        continue
    result[-1][1] = max(result[-1][1], sections[i][1])
for section in result:
    print(section[0], section[1])
