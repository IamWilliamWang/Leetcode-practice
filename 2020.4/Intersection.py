class Solution:
    def _f1(self, x):
        """
        第一条线的f(x)公式，当x超过合理范围时返回None
        :param x: x值
        :return: f(x)值，或None
        """
        if self.f1_limit_x[0] <= x <= self.f1_limit_x[1]:
            return self.k1 * x + self.b1
        return None

    def _f2(self, x):
        """
        第二条线的f(x)公式，当x超过合理范围时返回None
        :param x: x值
        :return: f(x)值，或None
        """
        if self.f2_limit_x[0] <= x <= self.f2_limit_x[1]:
            return self.k2 * x + self.b2
        return None

    def _listIntersect(self, list1: list, list2: list) -> list:
        """
        列表求交集，求的是list1 ∩ list2
        :param list1: 不含有重复数字的list
        :param list2: 不含有重复数字的list
        :return: 交集list
        """
        intersection_list = []
        for item in list1:
            if item in list2:
                intersection_list += [item]
        return intersection_list

    def _solveVerticalLines(self, start1: list, end1: list, start2: list, end2: list):
        """
        当其中一条是垂直线时的特殊处理函数
        :param start1:
        :param end1:
        :param start2:
        :param end2:
        :return:
        """
        # 如果两条都是垂直线
        if start1[0] == end1[0] and start2[0] == end2[0]:
            if start1[0] != start2[0]:  # 如果两条垂直线的x不一样
                self.special_result = None, None  # 保存特殊情况下的结果。不存在就是None, None
            else:  # 如果两条垂直线的x一样
                # 求出两条线的在y轴上最小和最大值
                f1_limit_y = [start1[1], end1[1]]
                f1_limit_y.sort()
                f2_limit_y = [start2[1], end2[1]]
                f2_limit_y.sort()
                # 求出在y轴上的重合范围
                common_range_y = set(range(f1_limit_y[0], f1_limit_y[1] + 1)).intersection(
                    set((range(f2_limit_y[0], f2_limit_y[1] + 1))))
                # common_range_y = self.listIntersect(list(range(f1_limit_y[0], f1_limit_y[1] + 1)),
                #                                     list(range(f2_limmit_y[0], f2_limmit_y[1] + 1)))
                if len(common_range_y) == 0:  # 如果没有重合
                    self.special_result = None, None
                else:  # 有重合的话返回重合部分最小的y值
                    common_range_y = list(common_range_y)
                    common_range_y.sort()
                    self.special_result = start1[0], common_range_y[0]
        # 只有第一条是垂直线
        elif start1[0] == end1[0]:
            # 求出第一条线的y值范围
            f1_limit_y = [start1[1], end1[1]]
            f1_limit_y.sort()
            # 求第二条线在这条线上的交点
            f2 = self._f2(start1[0])
            # 如果f2(x)有值，并且有交点
            if f2 is not None and f1_limit_y[0] <= f2 <= f1_limit_y[1]:
                self.special_result = start1[0], f2
            else:  # 没交点
                self.special_result = None, None
        # 只有第二条是垂直线，同理
        elif start2[0] == end2[0]:
            f2_limit_y = [start2[1], end2[1]]
            f2_limit_y.sort()
            f1 = self._f1(start2[0])
            if f1 is not None and f2_limit_y[0] <= f1 <= f2_limit_y[1]:
                self.special_result = start2[0], f1
            else:
                self.special_result = None, None

    def _initLineSegments(self, start1: list, end1: list, start2: list, end2: list) -> bool:
        """
        求两条线的k和b，x值范围
        :param start1:
        :param end1:
        :param start2:
        :param end2:
        :return: k和b都求出来了吗
        """
        exist_vertical_line = False  # 是否有垂直线
        self.f1_limit_x = [start1[0], end1[0]]
        self.f1_limit_x.sort()
        self.f2_limit_x = [start2[0], end2[0]]
        self.f2_limit_x.sort()
        # y=k(x-x0)+y0 -> y=kx+y0-kx0
        # 先算k1和b1（算完才能调用self._f1）
        x0, y0 = start1
        x1, y1 = end1
        if x0 == x1:
            exist_vertical_line = True
        else:
            self.k1 = (y1 - y0) / (x1 - x0)
            self.b1 = y0 - self.k1 * x0
        # 算k2和b2（算完才能调用self._f2）
        x0_2, y0_2 = start2
        x1_2, y1_2 = end2
        if x0_2 == x1_2:
            exist_vertical_line = True
        else:
            self.k2 = (y1_2 - y0_2) / (x1_2 - x0_2)
            self.b2 = y0_2 - self.k2 * x0_2
        if exist_vertical_line:  # 如果有垂直线，就调用特殊处理方法
            self._solveVerticalLines(start1, end1, start2, end2)
        return not exist_vertical_line

    def _getSmallXRange(self, attempt_X: list):
        """
        在取值范围缩小到1，返回x_min, x_max。如果没发现任何可能的解则返回None, None
        :param attempt_X: 所有可能取到的x值
        :return: x的最小值，x的最大值
        """
        last_result = None
        # 一直遍历计算f1(x)-f2(x)，直到发现符号改变为止
        for x in attempt_X:
            result = self._f1(x) - self._f2(x)
            if result == 0:
                return x, x
            if last_result is None:
                last_result = result
                continue
            if last_result * result < 0:
                return x - 1, x
            last_result = result
        return None, None

    def solve(self, begin_x: int, end_x: int):
        """
        使用二分查找法进行查找，返回解的x, y。如果没找到解则返回None, None
        :param begin_x: x的最小值
        :param end_x: x的最大值
        :return:
        """
        while True:
            mid_x = (begin_x + end_x) / 2
            # 求f1(x)-f2(x)=0的解
            f_mid = self._f1(mid_x) - self._f2(mid_x)
            if abs(f_mid) < 1e-7:  # 题目要求小于1e-6的误差
                return mid_x, self._f1(mid_x)
            elif mid_x - begin_x < 1e-8:
                return None, None
            if f_mid * (self._f1(begin_x) - self._f2(begin_x)) > 0:  # 同号
                begin_x = mid_x
            else:
                end_x = mid_x

    def intersection(self, start1: list, end1: list, start2: list, end2: list) -> list:
        # 初始化，求两条线的k和b。如果返回False就说明有线段的k求不出来（返回前已经处理完毕这种情况）
        if not self._initLineSegments(start1, end1, start2, end2):
            result_x, result_y = self.special_result  # 获取特殊解
        else:  # 正常的两条线
            # 获得两条线在x轴上的交集
            attempt_x = set(range(self.f1_limit_x[0], self.f1_limit_x[1] + 1)).intersection(
                set((range(self.f2_limit_x[0], self.f2_limit_x[1] + 1))))
            attempt_x_list = list(attempt_x)
            attempt_x_list.sort()
            # attempt_x_list = self._listIntersect(list(range(self.f1_limit_x[0], self.f1_limit_x[1] + 1)),
            #                                 list(range(self.f2_limit_x[0], self.f2_limit_x[1] + 1)))
            xmin, xmax = self._getSmallXRange(attempt_x_list)  # 把庞大的x轴范围缩小为长度为1的范围
            if xmin is None:  # 证明两条线在x轴上没交集
                return []
            result_x, result_y = self.solve(xmin, xmax)  # 二分查找法求解
        if result_x is None:  # 没有找到可行解
            return []
        else:
            return [result_x, result_y]


# print(Solution().intersection([0, 3], [0, 6], [0, 1], [0, 5]))  # [0, 3]
# print(Solution().intersection([0, 0], [1, 0], [1, 1], [0, -1]))  # [0.5, 0]
print(Solution().intersection([-30, 4], [-9, -30], [-25, -3], [0, -47]))
