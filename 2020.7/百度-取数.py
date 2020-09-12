from typing import List
from test_script import speedtest_format as speedtest
import random
import numpy as np


def moveNum(numsLen, maxRound, numbers: List[int], minuses: List[int]):
    """
    最多可以得到多少分
    :param numsLen: 数字个数
    :param maxRound: 回合数
    :param numbers:
    :param minuses:
    :return:
    """
    nums = zip(numbers, minuses)
    nums = list(nums)
    # nums.sort(key=lambda x: (x[1], x[0]), reverse=True)  # 每次减的多的排在前面
    nums.sort(reverse=True)
    nums.insert(0, (0, 0))  # 因为索引使用的1-based index

    dp = np.zeros((numsLen + 1, maxRound + 1), dtype=np.int)

    for roundIdx in range(1, maxRound + 1):
        for numberIdx in range(1, numsLen + 1):
            # 根据已有的战果，本回合抽出第numberIdx张牌，抽的时候再计算已经被减掉了多少
            drawCard = dp[numberIdx - 1][roundIdx - 1] + nums[numberIdx][0] - (nums[numberIdx][1] * (roundIdx - 1))
            # 本回合不抽出第numberIdx张牌，这张牌以后再抽。上面的公式不涉及dp[numberIdx][roundIdx - 1]可以避免重复抽
            noDrawCard = dp[numberIdx - 1][roundIdx]
            dp[numberIdx][roundIdx] = max(drawCard, noDrawCard)

    return dp[numsLen][maxRound]


def maxScore(numbersLength: int, maxRound: int, numbers: List[int], round_to_minus: List[int]):
    maxSum = 0
    numbers = sorted(numbers[:numbersLength], reverse=True)
    for _round, number in enumerate(numbers):
        if _round == maxRound:
            break
        number -= sum(round_to_minus[:_round])
        maxSum += number
    return maxSum


# speedtest([moveNum], (5, 5, [10, 20, 30, 40, 50], [4, 5, 6, 7, 8]))
speedtest([moveNum], (15, 15, [4, 1, 3, 19, 12, 9, 2, 9, 20, 11, 17, 9, 6, 2, 14], [17, 9, 0, 9, 11, 13, 10, 3, 8, 7, 14, 6, 2, 6, 17]))
speedtest([moveNum], (100, 100, [37, 0, 19, 41, 15, 38, 26, 48, 49, 10, 35, 40, 25, 22, 17, 27, 18, 1, 30, 6, 10, 14, 38, 6, 28, 48, 33, 47, 16, 17, 4, 46, 12, 28, 36, 50, 22, 26, 13, 6, 37, 50, 42, 5, 36, 16, 1, 34, 0, 27, 27, 20, 33, 39, 21, 22, 42, 32, 20, 18, 27, 32, 26, 25, 34, 50, 24, 5, 37, 34, 13, 24, 32, 41, 11, 43, 5, 21, 4, 48, 2, 35, 34, 28, 32, 43, 33, 49, 18, 24, 22, 37, 49, 43, 37, 19, 29, 12, 27, 47], [22, 46, 47, 14, 39, 36, 42, 9, 21, 13, 24, 14, 39, 32, 24, 9, 2, 21, 39, 18, 25, 43, 18, 11, 4, 2, 43, 24, 18, 20, 41, 8, 10, 45, 19, 4, 20, 5, 20, 14, 14, 6, 44, 8, 21, 46, 14, 37, 41, 11, 41, 11, 29, 40, 34, 22, 46, 46, 41, 21, 2, 48, 0, 38, 17, 14, 47, 21, 41, 44, 11, 37, 10, 31, 8, 2, 33, 15, 10, 34, 8, 2, 7, 47, 17, 1, 16, 39, 27, 49, 36, 6, 10, 41, 43, 8, 0, 36, 2, 0]))
# speedtest((moveNum, maxScore), (
#     random.randint(0, 50), random.randint(0, 50), [random.randint(0, 100) for _ in range(random.randint(0, 100))],
#     [random.randint(0, 100) for _ in range(random.randint(0, 100))]))
