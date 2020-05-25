from typing import List, Set


class Solution:
    def get分数(self, 分子: int, 分母: int) -> str:
        """
        获得已化简的分数的字符串。格式：分子/分母
        :param 分子:
        :param 分母:
        :return:
        """

        def 最大公因数(a: int, b: int):
            if b != 0:
                return 最大公因数(b, a % b)
            else:
                return a

        公因数 = 最大公因数(分子, 分母)
        return str(分子 // 公因数) + '/' + str(分母 // 公因数)

    def simplifiedFractions(self, n: int) -> List[str]:
        resultSet: Set[str] = set()  # 放置所有的分数
        分母List = list(range(2, n + 1))  # 分母不能为1
        for 分母 in 分母List:
            for i in range(1, 分母):  # 分子永远比分母小
                resultSet.add(self.get分数(i, 分母))
        resultList = list(resultSet)
        return sorted(resultList)


print(Solution().simplifiedFractions(2))
