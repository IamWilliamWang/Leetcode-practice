from functools import lru_cache


class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        @lru_cache(maxsize=None)
        def dp(restAmount: int):
            if restAmount == 0:
                return 0
            elif restAmount < coins[0]:
                return -1
            counts = []
            for coin in coins:
                result = dp(restAmount - coin)
                if result != -1:
                    counts.append(result)
            # print('dp(%d)=%d' % (restAmount,  1 + min(counts) if counts != [] else -1))
            return 1 + min(counts) if counts != [] else -1

        coins.sort()
        return dp(amount)

    def coinChangeNoRecusion(self, coins: list, amount: int) -> int:
        matrix = [0] * (amount + 1)
        coins.sort()
        for i in range(1, amount + 1):
            if i < coins[0]:
                matrix[i] = -1
                continue
            counts = []
            for coin in coins:
                if i-coin>=0 and matrix[i - coin] != -1:
                    counts.append(matrix[i - coin])
            matrix[i] = 1 + min(counts) if counts != [] else -1
            # print('matrix[%d]=%d'%(i,matrix[i]))
        return matrix[amount]


print(Solution().coinChange([1, 2, 5], 11))
