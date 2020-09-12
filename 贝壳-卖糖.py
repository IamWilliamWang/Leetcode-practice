days = 4
sells = [1, 3, 2, 4]
inPrice = [3, 2, 1, 100]
outPrice = 5
dp = [(outPrice - inPrice[0]) * sells[0]]
for i in range(1, days):
    bestInPrice = min(inPrice[:i + 1])  # 前n天的最低进价
    dp += [dp[-1] + (outPrice - bestInPrice) * sells[i]]
print(dp[-1])
