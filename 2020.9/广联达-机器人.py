from functools import reduce, lru_cache


def 最大公因数(l: list):
    def cal(a, b):
        while b:
            r = a % b
            a = b
            b = r
        return a

    return reduce(lambda x, y: cal(x, y), l)


def main():
    N, capicity = list(map(int, input().strip().split()))
    goods = []
    for _ in range(N):
        weight, value = list(map(float, input().strip().split()))
        value = int(value)
        weight = int(weight)
        goods += [[weight, value]]

    # tmp = 最大公因数([weight for (weight, _) in goods])
    # for i in range(N):
    #     goods[i][0] //= tmp
    # capicity //= tmp
    # goods.sort(key=lambda t: (-t[1], t[0]))
    # dp = [[0] * (capicity + 1) for _ in range(N + 1)]
    # for i in range(1, N + 1):
    #     for j in range(1, capicity + 1):
    #         dp[i][j] = max(dp[i - 1][j],
    #                        dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1] if j >= goods[i - 1][0] else 0)
    # print(dp[-1][-1])

    @lru_cache(maxsize=None)
    def dp(i: int, restCapcity: int, nowValue: float):
        nonlocal result
        if i == len(goods):
            result = max(result, nowValue)
            return
        dp(i + 1, restCapcity, nowValue)
        if restCapcity >= goods[i][0]:
            dp(i + 1, restCapcity - goods[i][0], nowValue + goods[i][1])

    result = 0
    dp(0, capicity, 0)
    print(result)


main()
