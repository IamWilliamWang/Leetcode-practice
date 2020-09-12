class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if not n:
        #     return False
        # import math
        # myLog = math.log(n, 3)
        # return math.fabs(myLog - int(myLog+1e-9)) < 1e-7
        def isPower(seedNumber: int, base: int):
            if seedNumber == n:
                return True
            elif seedNumber > n:
                return False
            base = base ** 2
            while base > 3 and seedNumber * base > n:
                base = base // 3
            return isPower(seedNumber * base, base)

        return isPower(1, 3)


print(Solution().isPowerOfThree(14348908))
