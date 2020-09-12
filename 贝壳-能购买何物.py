import bisect
from functools import reduce


def main():
    productCount = int(input().strip())
    productPrice = list(map(int, input().strip().split()))[:productCount]
    product = sorted([(price, i + 1) for i, price in enumerate(productPrice)])
    productPrice.sort()
    query = int(input().strip())
    for _ in range(query):
        # money一车, count一天几车, count天数 = list(map(int, input().strip().split()))
        myMoney = reduce(lambda x, y: x * y, list(map(int, input().strip().split())))
        if not productCount or myMoney < productPrice[0]:
            print(-1)
            continue
        if myMoney > productPrice[-1]:
            idx = productCount
        else:
            idx = bisect.bisect_left(productPrice, myMoney)
        if idx < productCount and productPrice[idx] == myMoney:  # 刚好能买到这个东西
            print(product[idx][1], product[idx][0])
        else:  # 买完还能剩余一点钱（指向要买的最后一个index）
            idx -= 1
            while idx > 0 and productPrice[idx] == productPrice[idx - 1]:
                idx -= 1
            print(product[idx][1], product[idx][0])


for _ in range(int(input().strip())):
    main()
