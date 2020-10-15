from math import factorial
from typing import List, Tuple

visited = set()
result = set()


def dp(i: int, nowSum: int, restMagic: int, nowList: List[tuple], usedMagicList: List[int]):
    """

    :param i: 当前指向array的第几个位置（开区间）
    :param nowSum: 当前的求和
    :param restMagic: 剩余的魔法技能数
    :param nowList: 记录当前保存的数字[(数, 索引), ……]
    :param usedMagicList: 记录使用过魔法技能的索引
    :return:
    """
    global result, visited
    if (i, nowSum, restMagic, tuple(nowList), tuple(usedMagicList)) in visited:
        return
    visited.add((i, nowSum, restMagic, tuple(nowList), tuple(usedMagicList)))
    if i == N:
        if nowSum == goodSum:
            # print(restMagic, nowList, usedMagicList)
            result.add((tuple(nowList), tuple(usedMagicList)))
        return
    if nowSum == goodSum:
        # print(restMagic, nowList, usedMagicList)
        result.add((tuple(nowList), tuple(usedMagicList)))
    if nowSum > goodSum:
        return
    dp(i + 1, nowSum + array[i], restMagic, nowList + [(array[i], i)], usedMagicList)
    dp(i + 1, array[i], magic, [(array[i], i)], [])
    if restMagic:
        dp(i + 1, nowSum + factorial(array[i]), restMagic - 1, nowList + [(array[i], i)], usedMagicList + [i])
        dp(i + 1, factorial(array[i]), magic - 1, [(array[i], i)], [i])


N, magic, goodSum = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))[:N]
dp(0, 0, magic, [], [])
print(len(result))
