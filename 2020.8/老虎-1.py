#
# 
# @param HP long长整型 HP
# @param ACK long长整型 ACK
# @param HP2 long长整型 HP2
# @param ACK2 long长整型 ACK2
# @return long长整型
#
import math


class Solution:
    def Pokemonfight(self, HP, ACK, HP2, ACK2):
        hp, ack, hpEnemy, ackEnemy = HP2, ACK2, HP, ACK
        if ackEnemy >= hp:  # 一回合被拍死
            return -1
        eatMadicine = False
        for round in range(1, 100000):
            hp -= ackEnemy  # 敌人攻击
            if hp <= 0:
                return -1
            if hp <= ackEnemy and hpEnemy > ack:  # 该考虑吃药了
                if eatMadicine:  # 发现不停的要吃药，没有机会攻击
                    return -1
                hp = HP2
                eatMadicine = True
            else:
                hpEnemy -= ack
                eatMadicine = False
            if hpEnemy <= 0:
                return round
        return -1


print(Solution().Pokemonfight(8, 3, 8, 1))
