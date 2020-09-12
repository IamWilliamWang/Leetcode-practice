from itertools import product

from test_script import speedtest, deprecated
from collections import defaultdict
from functools import lru_cache
import numpy as np


def main(_string=None):
    if _string is None:
        _string = input()
    strlen = len(_string)
    leftIndexList = [0] * strlen  # 记录左括号的位置
    matches = [0] * strlen  # 记录右匹配的位置
    dp = np.zeros((strlen, strlen, 3, 3), dtype=np.int)

    def getmatch(len):
        p = 0
        for i in range(len):
            if _string[i] == '(':
                leftIndexList[p] = i
                p = p + 1
            else:
                matches[i] = leftIndexList[p - 1]
                matches[leftIndexList[p - 1]] = i
                p = p - 1

    def dfs(l, r):
        if l + 1 == r:  # 边界条件
            dp[l][r][0][1] = 1
            dp[l][r][1][0] = 1
            dp[l][r][0][2] = 1
            dp[l][r][2][0] = 1
            return
        if matches[l] == r:  # 如果匹配的话方案数相加
            dfs(l + 1, r - 1)
            for i in range(3):
                for j in range(3):
                    if j != 1:
                        dp[l][r][0][1] = (dp[l][r][0][1] + dp[l + 1][r - 1][i][j])
                    if i != 1:
                        dp[l][r][1][0] = (dp[l][r][1][0] + dp[l + 1][r - 1][i][j])
                    if j != 2:
                        dp[l][r][0][2] = (dp[l][r][0][2] + dp[l + 1][r - 1][i][j])
                    if i != 2:
                        dp[l][r][2][0] = (dp[l][r][2][0] + dp[l + 1][r - 1][i][j])
            return
        else:  # 否则方案数相乘，乘法原理
            p = matches[l]
            dfs(l, p)
            dfs(p + 1, r)
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for q in range(3):
                            if not ((k == 1 and q == 1) or (k == 2 and q == 2)):
                                dp[l][r][i][j] = dp[l][r][i][j] + (dp[l][p][i][k] * dp[p + 1][r][q][j])

    getmatch(strlen)
    dfs(0, strlen - 1)
    ans = 0
    for i in range(3):
        for j in range(3):
            ans = (ans + dp[0][strlen - 1][i][j])
    return ans


@deprecated
def main2(string=None):
    @lru_cache(maxsize=None)
    def getTimesCount(s: str, l: int, r: int, lc: int, rc: int) -> int:
        if l >= r or s[l] != '(' or s[r] != ')':
            return 0
        if lc > rc:
            lc, rc = rc, lc
        if (lc, rc) != (BLACK, GREEN) and (lc, rc) != (BLACK, BLUE):
            return 0
        if r - l == 1:
            return 1
        ret = 0
        if getTimesCount(s, l + 1, r - 1, BLACK, GREEN):
            ret += getTimesCount(s, l + 1, r - 1, BLACK, GREEN) * 2  # GRGR BRGR
        if getTimesCount(s, l + 1, r - 1, GREEN, BLACK):
            ret += getTimesCount(s, l + 1, r - 1, GREEN, BLACK) * 2  # RGRG RGRB
        if getTimesCount(s, l + 1, r - 1, BLACK, BLUE):
            ret += getTimesCount(s, l + 1, r - 1, BLACK, BLUE) * 2
        if getTimesCount(s, l + 1, r - 1, BLUE, BLACK):
            ret += getTimesCount(s, l + 1, r - 1, BLUE, BLACK) * 2
        return ret

    BLACK, GREEN, BLUE = 0, 1, 2
    if string is None:
        string = '(())'
    return getTimesCount(string, 0, len(string) - 1, BLACK, GREEN) * 2 + getTimesCount(string, 0, len(string) - 1, BLACK, BLUE) * 2


# 题目：黑绿蓝三种颜色对括号染色。有两个限定条件：一对括号有且仅有一个被染色，相邻的彩色括号的颜色不能一样。求有多少种染色方案
def main3(s=None):
    def dp(index左边界, index右边界):
        if index左边界 + 1 == index右边界:  # 如果两个括号挨着的
            times所有位置的颜色[(index左边界, index右边界, black, green)] = times所有位置的颜色[(index左边界, index右边界, green, black)] = 1  # 左括号为黑，右括号为绿的方案有1种
            times所有位置的颜色[(index左边界, index右边界, black, blue)] = times所有位置的颜色[(index左边界, index右边界, blue, black)] = 1
            return
        if index与之匹配[index左边界] == index右边界:  # 说明不需要中间拆分，向内递归就好了
            dp(index左边界 + 1, index右边界 - 1)  # 向内递归，把里面的算好了
            for color左边界, color右边界 in product((black, green, blue), (black, blue)):  # 右边界向里不能紧接着就是绿色
                times所有位置的颜色[(index左边界, index右边界, black, green)] += times所有位置的颜色[(index左边界 + 1, index右边界 - 1, color左边界, color右边界)]
            for color左边界, color右边界 in product((black, blue), (black, green, blue)):
                times所有位置的颜色[(index左边界, index右边界, green, black)] += times所有位置的颜色[(index左边界 + 1, index右边界 - 1, color左边界, color右边界)]
            for color左边界, color右边界 in product((black, green, blue), (black, green)):
                times所有位置的颜色[(index左边界, index右边界, black, blue)] += times所有位置的颜色[(index左边界 + 1, index右边界 - 1, color左边界, color右边界)]
            for color左边界, color右边界 in product((black, green), (black, green, blue)):
                times所有位置的颜色[(index左边界, index右边界, blue, black)] += times所有位置的颜色[(index左边界 + 1, index右边界 - 1, color左边界, color右边界)]
            return
        # 不匹配，说明要拆分
        position分割字符串 = index与之匹配[index左边界]  # 找出左边的一对括号
        dp(index左边界, position分割字符串)  # 把这对括号拿去递归
        dp(position分割字符串 + 1, index右边界)  # 剩下的几个括号再拿去递归
        for color最前括号左, color第二个括号右, color最前括号右, color第二个括号左 in product(*([(black, green, blue)]*4)):
            if color最前括号右 == 0 or color第二个括号左 == 0 or color最前括号右 != color第二个括号左:  # 只有当两个都是彩色并且一样颜色才不可以上色
                times所有位置的颜色[(index左边界, index右边界, color最前括号左, color第二个括号右)] += times所有位置的颜色[(index左边界, position分割字符串, color最前括号左, color最前括号右)] * times所有位置的颜色[(position分割字符串 + 1, index右边界, color第二个括号左, color第二个括号右)]

    if s is None:
        s = '((()))'
    black, green, blue = 0, 1, 2
    index与之匹配 = [-1] * len(s)
    stackTmp = []
    for i, ch in enumerate(s):
        if ch == '(':
            stackTmp.append(i)
        else:
            index与之匹配[i] = stackTmp.pop()
            index与之匹配[index与之匹配[i]] = i
    times所有位置的颜色 = defaultdict(int)
    dp(0, len(s) - 1)
    return sum(times所有位置的颜色[(0, len(s) - 1, colorL, colorR)] for colorL, colorR in product((black, green, blue), (black, green, blue)))


if __name__ == '__main__':
    speedtest([main, main2, main3, lambda x: 12], ['(())'])
    speedtest([main, main2, main3, lambda x: 40], ['(()())'])
    speedtest([main, main2, main3, lambda x: 4], ['()'])
