import sys
from collections import defaultdict

N = int(input().strip())
classes = []
finalEndTime = 0
for _ in range(N):
    classes.append(list(map(int, input().strip().split())) + [1])  # [开始时间，结束时间Ex，该时段的线程数]
    finalEndTime = max(finalEndTime, classes[-1][1])
classes.sort()
# maxThreads = 0
# for i in range(1, N):
#     if classes[i][0] < classes[i - 1][1]:
#         classes[i][0] = max(classes[i][0], classes[i - 1][0])
#         classes[i][1] = min(classes[i][1], classes[i - 1][1])
#         classes[i][2] += classes[i - 1][2]
#         classes[i - 1] = None
#         maxThreads = max(maxThreads, classes[i][2])
# print(maxThreads)
counter = defaultdict(int)
maxThreads = 0
for _class in classes:
    for i in range(_class[0], _class[1]):
        counter[i] += 1
        maxThreads = max(maxThreads, counter[i])

print(maxThreads)
