#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param width int整型 要建的房屋面宽
# @param data int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
#
class Solution:
    def getHouses(self, width, data):
        centerPotential = []
        for i in range(0, len(data), 2):
            # 左边
            if i == 0:
                centerPotential.append(data[i] - data[i + 1] / 2 - width / 2)
            else:
                if (data[i] - data[i + 1] / 2) - (data[i - 2] + data[i - 1] / 2) >= width:
                    centerPotential.append((data[i] - data[i + 1] / 2) - width / 2)
            # 右边
            if i == len(data) - 2:
                centerPotential.append(data[i] + data[i + 1] / 2 + width / 2)
            else:
                if (data[i + 2] - data[i + 3] / 2) - (data[i] + data[i + 1] / 2) >= width:
                    centerPotential.append((data[i] + data[i + 1] / 2) + width / 2)
        return len(set(centerPotential))


print(Solution().getHouses(2, [-1, 4, 5, 2]))
