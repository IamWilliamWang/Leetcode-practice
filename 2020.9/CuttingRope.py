class Solution:
    def cuttingRope(self, n: int) -> int:
        def split(clipCount: int):
            if clipCount <= 1:
                raise ValueError
            # n = clipCount * a + b
            a = n // clipCount
            b = n % clipCount
            result = pow((a + 1), b) * pow(a, (clipCount - b))
            return result

        bestValue = 0
        count = 2
        while True:
            ret = split(count)
            if ret < bestValue:
                break
            bestValue = ret
            count += 1
        return bestValue


print(Solution().cuttingRope(10))
