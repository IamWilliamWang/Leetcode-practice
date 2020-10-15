from typing import List, Tuple


def minSwap(array, beginIdx, endIdx) -> int:
    def solve(begin, mid, end) -> int:
        retCount = 0
        subArrayI = 0
        sortedSubArray = [0] * (end - begin + 1)
        right = begin  # 起始指针均置于区间头部
        left = mid + 1
        for subArrayI in range(end - begin + 1):
            if right > mid or left > end:
                break
            if array[left] >= array[right]:
                sortedSubArray[subArrayI] = array[right]  # b中存放较小的数以实现升序排列
                right += 1
                subArrayI += 1
            else:
                sortedSubArray[subArrayI] = array[left]
                retCount += mid - right + 1  # 一旦左数列中有一项比后面一项大，则左数列中后面所有项均比后面那一项大。
                left += 1
                subArrayI += 1
        while right <= mid:  # 若某一段指针已经指到尾部，即其元素已经安置好，只需将另一段中剩下元素置入即可
            sortedSubArray[subArrayI] = array[right]
            right += 1
            subArrayI += 1
        while left <= end:
            sortedSubArray[subArrayI] = array[left]
            left += 1
            subArrayI += 1
        for subArrayI in range(end - begin + 1):
            array[begin + subArrayI] = sortedSubArray[subArrayI]  # 将b中元素复制进入a的相应位置
        return retCount

    if beginIdx == endIdx:
        return 0
    else:
        mid = (beginIdx + endIdx) // 2
        right = minSwap(array, beginIdx, mid)
        left = minSwap(array, mid + 1, endIdx)
        return right + left + solve(beginIdx, mid, endIdx)


n = int(input().strip())
colors = input().strip()
array = list(map(int, input().strip().split()))
print(minSwap(array, 0, len(array) - 1))
