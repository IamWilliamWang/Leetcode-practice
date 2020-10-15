n = int(input().strip())
mul = [0, 0, 0]
dp = [1]
dpLen = 1
while dpLen < n:
    choices = [dp[mul[0]] * 2, dp[mul[1]] * 3, dp[mul[2]] * 5]
    best = min(choices)
    if best != dp[-1]:
        dp.append(best)
        dpLen += 1
    mul[choices.index(best)] += 1
print(dp[-1])