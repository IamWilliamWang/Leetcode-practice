class HeapSort:
    """
    堆排序实现
    """

    def __init__(self, nums: list):
        """
        初始化要用的堆（不会改变原数组）
        :param nums: 要排序的数组
        """
        self._heap = [0] + nums  # 方便起见在最前处添加一个空位
        self._heapSize = len(nums)
        self._isMaxHeap = False

    def _adjust(self):
        """
        进行一次堆调整，返回本轮的结果
        :return: 如果是大顶堆返回的是第k个最小值，反之返回第k个最大值
        """
        for fatherIndex in range(self._heapSize // 2, 0, -1):
            childIndexes = [2 * fatherIndex, 2 * fatherIndex + 1] if (2 * fatherIndex + 1) <= self._heapSize else [2 * fatherIndex]
            rectangleNumbers = [self._heap[fatherIndex]] + [self._heap[childIndex] for childIndex in childIndexes]
            # 大顶堆是把小数字向上移动
            adjustIndexInRectangle = rectangleNumbers.index(min(rectangleNumbers)) if self._isMaxHeap else rectangleNumbers.index(max(rectangleNumbers))
            if adjustIndexInRectangle == 0:
                continue
            self._heap[fatherIndex], self._heap[childIndexes[adjustIndexInRectangle - 1]] = self._heap[childIndexes[adjustIndexInRectangle - 1]], self._heap[fatherIndex]
        self._heap[1], self._heap[self._heapSize] = self._heap[self._heapSize], self._heap[1]
        self._heapSize -= 1
        return self._heap[self._heapSize + 1]

    def getLastElements(self, lastElementsLengthInSortedList: int, reverse=False) -> list:
        """
        获得排序后的数组中最后length个元素
        :param lastElementsLengthInSortedList: 要在最后截取多长的数组
        :param reverse: 是否从大到小排序
        :return: 排好的数组后lastElementsLengthInSortedList个元素
        """
        self._isMaxHeap = reverse  # reverse排序就是大顶堆
        if lastElementsLengthInSortedList < 1:
            return []
        # 当没够时继续调整，直到达到要求或者排序结束
        while self._heapSize > 0 and (len(self._heap) - 1) - self._heapSize < lastElementsLengthInSortedList:
            self._adjust()
        return self._heap[self._heapSize + 1:]

    def sort(self, reverse=False) -> list:
        """
        获得排序后的数组
        :param reverse: 是否从大到小排序
        :return: 排好的数组
        """
        return self.getLastElements(self._heapSize, reverse)


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        if k < len(nums)//2:  # k比较小，要取的数比较靠后
            return HeapSort(nums).getLastElements(k)[0]  # 获得排序后截取最后长度为k的list，第k个最大值就是[0]
        # 如果k比较大，则将从大到小排序截取最后len(nums)-k+1个元素。例：nums=[1,2,3,4,5],k=4。反向排序后截取出[2,1]
        return HeapSort(nums).getLastElements(len(nums)-k+1, reverse=True)[0]  # 取得首个元素

import random
print(HeapSort([random.randint(0, 100) for _ in range(20)]).sort(True))
