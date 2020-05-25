import math
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def 解析为小于10的因子(self, num: int) -> tuple:
        # 先找出所有的[(因子, 因子), (因子, 因子)...]
        因子列表元组列表 = []
        for i in range(int(math.sqrt(num)), 0, -1):
            if num // i * i == num:
                因子列表元组列表 += [(i, num // i)]
                if 0 < i < 10 and 0 < num // i < 10:
                    return i, num // i
        # 想办法把>9的因子拆开
        for 因子元组 in 因子列表元组列表:
            因子列表 = list(因子元组)
            for i in range(len(因子列表)):
                if 因子列表[i] >= 10:  # 只拆开>9的数字
                    if 因子列表[i] == num:  # 避免重复调用自身，导致无限递归
                        continue
                    分解后的因子 = list(self.解析为小于10的因子(因子列表[i]))
                    if 分解后的因子:  # 把当前换成分解后的因子
                        因子列表.pop(i)
                        for j in range(len(分解后的因子) - 1, -1, -1):
                            因子列表.insert(i, 分解后的因子[j])
            # 拆分完毕后看看符不符合因子全<10
            if max(因子列表) < 10:
                return tuple(因子列表)
        return ()  # 没有满足题意的因子列表

    def smallestFactorization(self, a: int) -> int:
        # 解析为小于10的因子列表
        满足题目要求的list = list(self.解析为小于10的因子(a))
        满足题目要求的list.sort()
        # 如果头一个是1，踢出去
        if 满足题目要求的list != [] and 满足题目要求的list[0] == 1:
            满足题目要求的list.pop(0)
        # 找找有没有相邻的数字可以乘起来，进行合并
        for i in range(len(满足题目要求的list) - 2, -1, -1):
            if 满足题目要求的list[i] * 满足题目要求的list[i + 1] < 10:
                满足题目要求的list[i] = 满足题目要求的list[i] * 满足题目要求的list[i + 1]
                满足题目要求的list.pop(i + 1)
        满足题目要求的list.sort()
        # 含有各个因子的tuple转成int
        result = 0
        for 单位数字 in 满足题目要求的list:
            result = 10 * result + 单位数字
        return result


print(Solution().smallestFactorization(256))
