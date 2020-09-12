def binary_search(nums, target, mode=0, key=None):
    """
    二分查找法，返回target出现的位置，找不到返回-1。也可以搜索左边界(首次出现的位置)和右边界(最后出现的位置)，找不到返回-1
    :param nums: 整形或者object数组（默认为升序）
    :param target: 要查找的数字或者object（如果是数组里的是object而target是其里面的变量则需要传入key；如果数组和target是同一个类则需要实现该类的__lt__, __gt__和__eq__）
    :param mode: 0为二分查找，1为左边界搜索，2为右边界搜索
    :param key: 搜索时用什么值进行比较
    :return:
    """
    if key is None:  # 如果没指定，那么生成默认的key函数
        key = lambda element: element
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if key(nums[mid]) < target:
            left = mid + 1
        elif key(nums[mid]) > target:
            right = mid - 1
        elif key(nums[mid]) == target:
            if mode == 1:
                right = mid - 1  # 收缩左侧边界
            elif mode == 2:
                left = mid + 1  # 收缩左侧边界
            else:  # mode==0
                return mid  # 直接返回
        else:
            raise ValueError(
                'The search was accidentally terminated. Check whether the key function returns the specified output')
    if mode == 1:
        # 最后要检查 left 越界的情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    elif mode == 2:
        # 最后要检查 right 越界的情况
        if right < 0 or nums[right] != target:
            return -1
        return right
    else:  # mode==0
        return -1


class Section:
    def __init__(self, begin: int, stopInc: int):
        self._begin = begin
        self._stop = stopInc
        self.sum = sumOf(self._begin, self._stop)

    def getBegin(self):
        return self._begin

    def setBegin(self, x):
        self._begin = x
        self.sum = sumOf(self._begin, self._stop)

    def getStop(self):
        return self._stop

    def setStop(self, x):
        self._stop = x
        self.sum = sumOf(self._begin, self._stop)

    def __eq__(self, other):
        assert type(other) == int
        return self._begin <= other <= self._stop

    def __gt__(self, other):
        assert type(other) == int
        return self._begin > other

    def __lt__(self, other):
        assert type(other) == int
        return self._stop < other

    def __str__(self):
        return '(%d, %d)' % (self._begin, self._stop)


def sumOf(start: int, stopInc: int):
    if not start:
        return sums[stopInc]
    return sums[stopInc] - sums[start - 1]


N = int(input().strip())
weights = [0] + list(map(int, input().strip().split()))[:N]  # 和整个题目的1-based idx保持一致
pops = list(map(lambda s: int(s), input().strip().split()))[:N]
sums, sumNum = [], 0
for num in weights:
    sumNum += num
    sums.append(sumNum)
sections = [Section(1, N)]
for popIdx in pops:
    splitIdx = binary_search(sections, popIdx)  # 找出第几个区间需要切开
    start, end = sections[splitIdx].getBegin(), sections[splitIdx].getStop()
    sections[splitIdx].setStop(popIdx - 1)
    if popIdx + 1 <= end:
        sections.insert(splitIdx + 1, Section(popIdx + 1, end))
    if sections[splitIdx].getBegin() > sections[splitIdx].getStop():
        del sections[splitIdx]
    print(max([sec.sum for sec in sections], default=0))
