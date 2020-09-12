#
#
# @param N int整型
# @return int整型
#
class Solution:
    def GetCoinCount(self, N):
        # write code here
        找零money = 1024 - N
        coins = [0, 0, 0, 0]
        coinSize = [64, 16, 4, 1]
        for i in range(len(coinSize)):
            coins[i] = 找零money // coinSize[i]
            找零money -= coinSize[i] * coins[i]
        return sum(coins)


print(Solution().GetCoinCount(200))
