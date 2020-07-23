class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        last = 0
        array = list(range(n))
        index = 0
        while array:
            index = index + m - 1
            index = index % len(array)
            last = array.pop(index)
        return last
