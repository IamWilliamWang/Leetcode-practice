from functools import lru_cache


class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(rest: int, mustDivide=False) -> int:
            if rest == 1:
                return 1
            result = [] if mustDivide else [rest]  # 不切分
            for i in range(1, rest // 2 + 1):  # 分成两个数字
                if rest - i < 1:
                    break
                result.append(i * dp(rest - i))  # i和rest-i两个数字
            return max(result)

        return dp(n, True)


print(Solution().integerBreak(10))
