import random


class Solution:
    def countTree(self, nowNumber: int, maxNumber: int) -> int:
        """
        统计根节点为nowNumber的十叉树的节点总数。叶子节点代表的数字不可以超过maxNumber
        :param nowNumber:
        :param maxNumber:
        :return:
        """
        startAt = nowNumber  # 这一层开始统计的数字
        endAt = nowNumber + 1  # 这一层结束统计数字的下一个
        result = 0
        while startAt <= maxNumber:  # 如果没超过最大值，进行统计
            result += min(endAt, maxNumber + 1) - startAt  # 加上这一层的节点个数
            startAt *= 10  # 继续统计下一层树
            endAt *= 10  # 下一层的结束条件刚好是*10
        return result

    def findKthNumber(self, maxNumber: int, findIndex: int) -> int:  # 最大值和要找的索引值
        index = 1
        nowNumber = 1
        while index < findIndex:  # 如果索引值没要到达
            当前数字加一时索引要加多少 = self.countTree(nowNumber, maxNumber)
            # 如果当前的高位数可以跳过（按层一位一位进行确定）
            if index + 当前数字加一时索引要加多少 <= findIndex:
                index += 当前数字加一时索引要加多少  # 跳过当前的高位数
                nowNumber += 1  # 当前的高位数加1
            else:
                if index == findIndex:  # 如果刚好碰到了要求的是根节点
                    break
                index += 1  # 索引值为当前树的第一个子节点
                nowNumber *= 10  # 变成第一个子节点的数字
        return nowNumber

        # @lru_cache(maxsize=None)
        # def subCountMaxEx(suffixNumber):
        #     diff = len(str(maxNumber)) - len(str(suffixNumber))
        #     return pow(10, diff) if diff != 0 else 0
        # @lru_cache(maxsize=None)
        # def subCountMaxInc(suffixNumber):
        #     return subCountMaxEx(suffixNumber) + 1
        #
        # nowIndex = 1
        # nowNumber = 1
        # while nowNumber <= maxNumber:
        #     if nowIndex == findIndex:
        #         return nowNumber
        #     # 先在高位上大步向前走
        #     while nowNumber + subCountMaxEx(nowNumber) < maxNumber:
        #         if nowIndex + subCountMaxInc(nowNumber) > findIndex:
        #
        #         nowNumber += 1
        #         nowIndex += subCountMaxInc(nowNumber)
        #     if nowIndex + subCountMaxInc(nowNumber) == findIndex:
        #         return nowNumber + 1
        #     # if nowIndex+subCountMaxInc(nowNumber)>findIndex:
        #     #     nowNumber=(findIndex-nowIndex)+10*nowNumber
        #     # 高位已固定，向下移一位进行探索
        #     nowNumber *= 10
        #     nowIndex += 1
        # return -1


def test():
    def ground_truth(n, k):
        l = [str(x) for x in range(1, n + 1)]
        l.sort()
        return int(l[k - 1])

    for _ in range(20):
        problem = [random.randint(0, 100) for _ in range(2)]
        truth = 0
        try:
            truth = ground_truth(problem[0], problem[1])
        except:
            continue
        ans = Solution().findKthNumber(problem[0], problem[1])
        if ans != truth:
            print('problem:', problem)
            print(ans, 'truth:', truth)
        else:
            print('Answer correct!')


test()
