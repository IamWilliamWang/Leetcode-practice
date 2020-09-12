class Solution:
    def minFlips(self, target: str) -> int:
        def dp(i: int, rotateCount: int) -> None:
            nonlocal ansMin
            if i >= len(target):
                ansMin = min(ansMin, rotateCount)
                return
            if (int(target[i]) + rotateCount) % 2 == 0:
                dp(i + 1, rotateCount)
            else:
                dp(i + 1, rotateCount + 1)

        ansMin = 2 ** 31
        dp(0, 0)
        return ansMin


print(Solution().minFlips('10111'))
print(Solution().minFlips('101'))
print(Solution().minFlips('00000'))
print(Solution().minFlips('001011101'))
