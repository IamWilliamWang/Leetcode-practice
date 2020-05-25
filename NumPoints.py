from typing import List
from math import sqrt


class Solution:
    def distance(self, pointX: List[int], pointY: List[int]) -> float:
        return sqrt((pointX[0] - pointY[0]) ** 2 + (pointX[1] - pointY[1]) ** 2)

    def parseXYList(self, points: List[List[int]], r: int):
        distanceMatrix = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self.distance(points[i], points[j])
                distanceMatrix[i, j] = distanceMatrix[j, i] = distance
        deletedPointsIndex = self.getDeletedPointsIndex(distanceMatrix, r)
        finallyDeletedPointsIndex = []
        lens=[]
        for i, j in deletedPointsIndex:
            distanceMatrixCopy=distanceMatrix.copy()
            tmp=[]
            for x,y in distanceMatrixCopy:
                if x==j or y==j:
                    tmp.append((x,y))
            for t in tmp:
                del distanceMatrixCopy[t]
            ansLen=len(self.getDeletedPointsIndex(distanceMatrixCopy,r))
            lens.append((i,ansLen))
            distanceMatrixCopy = distanceMatrix.copy()
            tmp = []
            for x, y in distanceMatrixCopy:
                if x == i or y == i:
                    tmp.append((x, y))
            for t in tmp:
                del distanceMatrixCopy[t]
            ansLen = len(self.getDeletedPointsIndex(distanceMatrixCopy, r))
            lens.append((j,ansLen))
            # indexes = list(range(len(points)))
            # indexes.remove(i)
            # indexes.remove(j)
            # count1, count2 = 0, 0
            # for index in indexes:
            #     if (i, index) in distanceMatrix and distanceMatrix[i, index] > r*2:
            #         count1 += 1
            # for index in indexes:
            #     if (j, index) in distanceMatrix and distanceMatrix[j, index] > r*2:
            #         count2 += 1
            # if count1 != 0 or count2 != 0:
            #     finallyDeletedPointsIndex.append(i if count1 > count2 else j)
        lens=sorted(lens,key=lambda t:t[1])
        xList, yList = [], []
        for i in range(len(points)):
            if i == lens[0][0]:
                continue
            x, y = points[i]
            xList.append(x)
            yList.append(y)
        return xList, yList

    def getDeletedPointsIndex(self, distanceMatrix, r):
        deletedPointsIndex = []
        for i, j in distanceMatrix:
            if distanceMatrix[i, j] > r*2:
                deletedPointsIndex.append([i, j])
        for i in range(len(deletedPointsIndex) - 1, 0, -2):
            del deletedPointsIndex[i]
        return deletedPointsIndex

    def numPoints(self, points: List[List[int]], r: int) -> int:
        xList, yList = self.parseXYList(points, r)
        circleX = sum(xList) / len(xList)
        circleY = sum(yList) / len(yList)
        resultCount = 0
        for i in range(len(circleX)):
            if self.distance([circleX, circleY], [xList[i], yList[i]]) <= r:
                resultCount += 1
        return resultCount


print(Solution().numPoints(points=[[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5))
