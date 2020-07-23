from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = [0] * (1 + max(len(a), len(b)))
        i = len(result) - 1
        for first, second in zip_longest(reversed(a), reversed(b)):
            first = int(first) if first is not None else -1
            second = int(second) if second is not None else -1
            if first == -1 or second == -1:
                result[i] += first if second == -1 else second
            else:
                result[i] += first + second
            if result[i] > 1:
                result[i] -= 2
                result[i - 1] += 1
            i -= 1
        while result and result[0] == 0:
            result = result[1:]
        if not result:
            result = [0]
        return ''.join([str(binary) for binary in result])
