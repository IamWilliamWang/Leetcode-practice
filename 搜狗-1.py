#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能交换奖品的最大数量
# @param a int整型
# @param b int整型
# @param c int整型
# @return int整型
#
class Solution:
    def numberofprize(self, a, b, c):
        cards = sorted([a, b, c])
        result = 0
        while True:
            cards[2] -= 1
            cards.sort()
            cards[2] -= 1
            cards.sort()
            cards[0] += 1
            cards.sort()
            if cards[0] >= result:
                result = cards[0]
            else:
                break
        return result


print(Solution().numberofprize(9, 3, 3))
