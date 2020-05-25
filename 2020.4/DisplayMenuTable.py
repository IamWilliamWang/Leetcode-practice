import numpy as np


class Solution:
    def gernerateTitleList(self,orders: list):
        titleList=[]
        for orderItem in orders:
            if orderItem[2] not in titleList:
                titleList.append(orderItem[2])
        titleList.sort()
        titleList.insert(0,'Table')
        return titleList

    def displayTable(self, orders: list) -> list:
        resultMatrix = []  # 不包含标题的int结果矩阵
        # titleList = ['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water']
        titleList = self.gernerateTitleList(orders)
        def findTableIndexInResult(tableId: int):
            for i in range(len(resultMatrix)):
                if resultMatrix[i][0] == tableId:
                    return i
            return -1

        for orderItem in orders:
            if findTableIndexInResult(int(orderItem[1])) == -1:
                row = [int(orderItem[1])] + [0 for _ in range(len(titleList)-1)]
                resultMatrix.append(row)
            resultMatrix[findTableIndexInResult(int(orderItem[1]))][titleList.index(orderItem[2])] += 1
        resultMatrix.sort()
        resultMatrixStr = [titleList.copy()]
        for resultRow in resultMatrix:
            resultMatrixStr.append(list(map(str,resultRow)))
        return resultMatrixStr


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(Solution().displayTable(orders))
