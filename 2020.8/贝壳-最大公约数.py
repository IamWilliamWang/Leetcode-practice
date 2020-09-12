from functools import lru_cache
from itertools import islice
from math import sqrt


class Prime:
    """
    获得素数数组的高级实现。支持 in 和 [] 运算符，[]支持切片
    """

    def __init__(self):
        self._list = [2, 3, 5, 7, 11, 13]  # 保存所有现有的素数列表

    def __contains__(self, n: int) -> bool:
        """
        判断n是否是素数
        :param n: 要判断的素数
        :return: 是否是素数
        """
        if not n % 2:  # 偶数只有2是素数
            return n == 2
        a, b = self.indexOf(n)  # 搜索n在素数列表中的位置
        return a == b  # 如果a b相同，代表这就是n在素数列表中的位置

    def __getitem__(self, i):
        """
        i为正整数时返回第i个元素；i为slice时返回切片数组（当i.stop=None时只返回迭代器）
        :param i: index或者slice
        :return: int或list或iterator
        """
        if isinstance(i, slice):  # 如果i是切片
            it = self.range(i.start, i.stop, i.step)  # 获得迭代器
            if i.stop:  # 如果指定了stop，则返回对应的数组
                return list(it)
            return it  # 没指定就直接返回迭代器
        else:  # 如果n是正整数
            self._extendToLen(i + 1)  # 拓展list长度直到n
            return self._list[i]  # 返回第n个元素

    def indexOf(self, n: int):
        """
        获得数字n位于素数列表的第几个位置，或者哪两个位置之间
        :param n: 要搜索的素数
        :return: 如果搜到则返回(index, index)；搜不到则返回n的大小在哪两个相邻位置之间(from, to)
        """
        if n < 2:
            return -1, 0
        if n > self._list[-1]:  # 需要拓展列表
            self._extend(n)
        import bisect
        index = bisect.bisect(self._list, n)  # 二分法搜索大于n的最左边位置
        if self._list[index - 1] == n:
            return index - 1, index - 1
        else:
            return index - 1, index

    def range(self, start=0, stop=None, step=1) -> islice:
        """
        获得素数数组的range迭代器
        :return: 迭代器
        """
        if stop:  # 如果有指明stop的话
            self._extendToLen(stop + 1)  # 拓宽list到stop位置
            return islice(self._list, start, stop, step)  # 生成切片后的迭代器
        return islice(self, start, None, step)  # 只有没指定stop时制造迭代器的切片，返回指向n.start位置的迭代器

    def primeRange(self, minN: int, maxN: int, step=1):
        """
        返回包含[minN, maxN)内所有素数的迭代器
        :param minN: 素数最小值
        :param maxN: 素数最大值（不包括）
        :param step: 遍历的步伐，默认为1
        :return: 迭代器
        """
        minN = max(2, minN)  # 开始值合法化
        if minN >= maxN:  # 异常参数检查
            return
        self._extend(maxN)  # 拓展list直到包含stop
        i = self.indexOf(minN)[1]  # 找到startN所在的位置，或者startN可以插入的位置
        beginning_i = i
        while i < len(self._list):  # 防止数组越界（其实不会，因为extend过了，一定是break之前就return）
            p = self._list[i]  # 获取第i个元素
            if p < maxN:  # 每次必须小于maxN才能yield
                if (i - beginning_i) % step == 0:
                    yield p
                i += 1
            else:  # 超过范围就跳出
                return

    def _extend(self, n: int) -> None:
        """
        拓展素数列表直到涵盖范围包括数字n就立刻停止
        :param n: 将素数列表拓展到哪个数字为止
        :return:
        """
        if n <= self._list[-1]:  # 如果list已经包含，则不需要拓展
            return
        maxSqrt = int(n ** 0.5) + 1  # 要拓展到的位置
        self._extend(maxSqrt)  # 如果列表没有拓展到sqrt(n)，递归拓展
        begin = self._list[-1] + 1  # 从哪里开始搜索
        sizer = [i for i in range(begin, n + 1)]  # 生成所有数字的数组
        for prime in self.primeRange(2, maxSqrt):  # 得到[2,maxSqrt)所有的素数
            for i in range(-begin % prime, len(sizer), prime):
                sizer[i] = 0  # 把所有非素数变为0
        self._list += [x for x in sizer if x]  # 删去所有的零，剩下的就是素数列表

    def _extendToLen(self, listLen: int) -> None:
        """
        将素数列表的长度至少拓展到listLen
        :param listLen: 至少拓展到多长
        :return:
        """
        while len(self._list) < listLen:  # 每次n*1.5，直到list长度符合要求
            self._extend(int(self._list[-1] * 1.5))


prime = Prime()


def _input():
    import sys
    return sys.stdin.readline()


def get因子Set(number: int) -> set:
    yinziList = [1, number]
    for i in range(2, int(sqrt(number)) + 1):
        if i not in prime:  # 因子都是素数
            continue
        if number % i == 0:
            yinziList.append(i)
            yinziList.append(number // i)
    return set(yinziList)


def main():
    N = int(_input().strip())
    array = list(map(int, _input().strip().split()))[:N]
    if not N:
        print(0)
        return
    array因子 = [get因子Set(num) for num in array]
    tmp = array因子[0]
    for yinzi in array因子:
        tmp.intersection_update(yinzi)
    if len(tmp) > 1:  # 所有的set有公共区域
        print(-1)
        return
    minDelete = 2 ** 31 - 1
    interStack = []

    @lru_cache(maxsize=None)
    def dp(i: int, deleteCount: int):
        nonlocal minDelete
        if i >= len(array因子):
            if interStack and interStack[-1] == {1}:
                minDelete = min(minDelete, deleteCount)
            return
        stackEmpty = not interStack
        interStack.append(array因子[i] if stackEmpty else array因子[i].intersection(interStack[-1]))
        dp(i + 1, deleteCount)  # 不删除该位置
        interStack.pop()
        if not stackEmpty:
            interStack.append(interStack[-1])
        dp(i + 1, deleteCount + 1)
        if not stackEmpty:
            interStack.pop()

    # dp(0, 0)
    array因子.sort(key=lambda x:list(x))
    count=0
    for i in range(len(array因子)-1,0,-1):
        if i==0:
            continue
        yinzi = array因子[i]
        if yinzi.issuperset(array因子[i-1]):
            count+=1
            del array因子[i]
    dp(0,0)
    minDelete+=count
    print(minDelete if minDelete < 2 ** 30 else -1)


if __name__ == '__main__':
    for round in range(int(_input().strip())):
        main()
