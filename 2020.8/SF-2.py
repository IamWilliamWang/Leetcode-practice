# import bisect
# from functools import lru_cache
#
#
# def get服务器Idx(所需带宽):
#     return bisect.bisect_left(array带宽, 所需带宽)
#
#
# @lru_cache(maxsize=None)
# def dp(custmerPtr: int, goodsPtr: int, nowMoney: int):
#     global result
#     if custmerPtr >= customerCount or goodsPtr >= N服务器:
#         result = max(result, nowMoney)
#         return
#     idx服务器 = get服务器Idx(customers[custmerPtr][0])
#     if idx服务器 != len(array带宽) and idx服务器 >= goodsPtr:
#         dp(custmerPtr + 1, idx服务器 + 1, nowMoney + customers[custmerPtr][1])
#     dp(custmerPtr + 1, idx服务器, nowMoney)
#
#
# N服务器, customerCount = list(map(int, input().strip().split()))
# array带宽 = list(map(int, input().strip().split()))
# array带宽.sort()
# customers = []
# for _ in range(customerCount):
#     customers.append(tuple(map(int, input().strip().split())))
# customers.sort(key=lambda t: (t[0], -t[1]))  # 同样的贷款最多钱的优先
# result = 0
#
# dp(0, 0, 0)
# print(result)
import bisect

N服务器, customerCount = list(map(int, input().strip().split()))
array带宽 = list(map(int, input().strip().split()))
array带宽.sort()
customers = []
for _ in range(customerCount):
    customers.append(tuple(map(int, input().strip().split())))
customers.sort(key=lambda t: (t[0], -t[1]))  # 同样的贷款最多钱的优先
best = [0] * len(array带宽)


def get服务器Idx(所需带宽):
    return bisect.bisect_left(array带宽, 所需带宽)


for customer in customers:
    idx服务器 = get服务器Idx(customer[0])
    if idx服务器 == len(array带宽):
        continue
    best[idx服务器] = max(best[idx服务器], customer[1])
print(sum(best))
