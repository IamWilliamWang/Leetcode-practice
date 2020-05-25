import sys


class Dictionary:
    def __init__(self):
        self._keyList = []
        self._valueList = []

    def __contains__(self, item):
        return self.containsKey(item)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __len__(self):
        return len(self._keyList)

    def __str__(self):
        return str(self.__len__())

    def containsKey(self, key):
        return [key] in self._keyList

    def set(self, key, value):
        if not self.containsKey(key):
            self._keyList.append([key])
            self._valueList.append([value])
        else:
            self._valueList[self._keyList.index([key])] = [value]

    def get(self, key):
        if self.containsKey(key):
            return self._valueList[self._keyList.index([key])][0]
        return None


coins = list(map(int, sys.stdin.readline().strip().split()))
sum_n = int(sys.stdin.readline().strip())
dict = Dictionary()


def dp(c: list, n: int):
    if c in dict:
        return dict[c]
    if len(c) == 0:
        return -1
    if len(c) == 1:
        return 1 if c[0] == n else -1
    potentialResult = []
    for i in range(len(c)):
        removedOneElementC = c.copy()
        removedOneElementC.pop(i)
        potentialResult += [dp(removedOneElementC, n - c[i])]
    positiveResult = [result if result != -1 else 65535 for result in potentialResult]
    minI = positiveResult.index(min(positiveResult))
    dict[c] = 1 + positiveResult[minI] if positiveResult[minI] != 65535 else -1
    return dict[c]


print(dp(coins, sum_n))
