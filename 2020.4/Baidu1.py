import sys


class Solution:
    def _removeAt(self, l: list, index: int):
        """
        拷贝后，去掉list中的某一位置的元素
        :param l:
        :param index:
        :return:
        """
        newList = l.copy()
        newList.pop(index)
        return newList

    def maxCount(self, numbers: list, minus: list):
        self.maxPerRound = {}  # 存储每一回合可取到的最大分数，作为回溯的依据
        def dp(restElements: list, round: int):
            """
            获得当前状态下最多可获得多少分
            :param restElements: 拿剩下的a数组
            :param round: 第几回合（从0开始）。题目上是先取走数，后减值。为了方便我先减值后取数，在minus前面加[0]，这样round 0就不会减数字了
            :return:
            """
            # base case
            if restElements == []:
                return 0
            if round >= len(minus):
                return 0
            # 每个元素减去minus[round]
            restElements = [element - minus[round] for element in restElements]
            # 算子问题的最优解
            result = []
            for i in range(len(restElements)):
                result.append(restElements[i] + dp(self._removeAt(restElements, i), round + 1))  # 拿出任意一个数放到下一层
            ans = max(result) if result != [] else 0  # 计算当前状态下的最大分数
            # 存储最大分数以便回溯
            if round not in self.maxPerRound or (round in self.maxPerRound and self.maxPerRound[round] < ans):
                self.maxPerRound[round] = ans
            return ans
        minus = [0] + minus  # 保证执行时与题目相一致
        return dp(numbers, 0)

    def parsePath(self, minus: list):
        """
        根据每一回合可取到的最大分数，求出每一回合的决策
        :param minus:
        :return:
        """
        # 将dict的key作为index，value作为list[index]
        level2Path = [0] * (max(self.maxPerRound.keys()) + 1)
        for key in self.maxPerRound:
            level2Path[key] = self.maxPerRound[key]
        # 因为每一层的决策最后是相加的关系，所以统一前面的减去后面的就是该层加了多少分数
        for i in range(0, len(level2Path) - 1):
            level2Path[i] = level2Path[i] - level2Path[i + 1]
        # 将每个数字，每次被减掉的部分重新加上来
        for i in range(len(level2Path)):
            for j in range(i):
                level2Path[i] += minus[j]
        return level2Path


numbers_count = int(input().strip())  # 题目上要输入这个，实际上没一点用
minus_count = int(input().strip())  # 题目上要输入这个，实际上没一点用
numbers = list(map(int, sys.stdin.readline().strip().split()))
minus = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
minus.sort()
solution = Solution()
print(solution.maxCount(numbers, minus))
print('决策:', solution.parsePath(minus), '相加过程:', solution.maxPerRound)
# @Deprecated 笔试时的做法：
# matrix = [[x] * minus_count for x in numbers]
# for row_index in range(len(matrix)):
#     for i in range(1, minus_count):
#         matrix[row_index][i] -= sum(minus[:i])
# result = 0
# for i in range(minus_count):
#     result += max(matrix[i])
# sys.stdout.write(result)
