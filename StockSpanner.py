class StockSpanner:

    def __init__(self):
        self._stackPrice = [2 ** 31 - 1]
        self._stackIndex = [-1]
        self._index = 0

    def next(self, price: int) -> int:
        while self._stackPrice[-1] <= price:
            self._stackPrice.pop()
            self._stackIndex.pop()
        ret = self._index - self._stackIndex[-1]
        self._stackPrice.append(price)
        self._stackIndex.append(self._index)
        self._index += 1
        return ret
