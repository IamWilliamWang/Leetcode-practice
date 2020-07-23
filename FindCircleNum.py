from test_script import speedtest

from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        friendCircles: List[set] = []
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    iCircleIndex = -1
                    for circleI, circleSet in enumerate(friendCircles):
                        if i in circleSet:
                            iCircleIndex = circleI
                    if iCircleIndex >= 0:
                        friendCircles[iCircleIndex].add(j)
                    else:
                        friendCircles.append({j})
        for i in range(len(friendCircles) - 2, -1, -1):
            for j in range(len(friendCircles) - 1, i, -1):
                if friendCircles[i].intersection(friendCircles[j]):
                    friendCircles[i] = friendCircles[i].union(friendCircles[j])
                    del friendCircles[j]
        return len(friendCircles)


speedtest([Solution().findCircleNum, lambda x: 2], [
    [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]])
speedtest([Solution().findCircleNum, lambda x: 1], [
    [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]])
speedtest([Solution().findCircleNum, lambda x: 1], [
    [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]])
