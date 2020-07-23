from typing import List
from test_script import timer


class Solution:
    @timer
    def equationsPossible(self, equations: List[str]) -> bool:
        if not equations:
            return True
        # 相等的公式放前面，先处理相等后处理不等
        equalEquations, notEqualEquations = [], []
        for equation in equations:
            if equation[1:3] == '==':
                equalEquations.append(equation)
            else:
                notEqualEquations.append(equation)
        equations = equalEquations + notEqualEquations
        # 开始处理所有的equation
        equalSetList: List[set] = []
        for equation in equations:
            if equation[1:3] == '==':  # 处理等于的情况
                if equation[0] == equation[-1]:  # 自己一定等于自己
                    continue
                leftIndex, rightIndex = None, None
                for i, equalSet in enumerate(equalSetList):
                    if equation[0] in equalSet:
                        leftIndex = i
                    if equation[-1] in equalSet:
                        rightIndex = i
                if leftIndex is not None and rightIndex is not None and leftIndex != rightIndex:  # 两个都不是None，比较所在的组号
                    union = equalSetList[leftIndex].union(equalSetList[rightIndex])
                    if leftIndex < rightIndex:
                        del equalSetList[rightIndex]
                        del equalSetList[leftIndex]
                    else:
                        del equalSetList[leftIndex]
                        del equalSetList[rightIndex]
                    equalSetList.append(union)
                elif leftIndex is None and rightIndex is None:  # 两个都是None，新建新组添加这两个
                    equalSetList += [{equation[0], equation[-1]}]
                    continue
                elif leftIndex is None:  # 左边的是None，就把左边加到右边对应的组
                    equalSetList[rightIndex].add(equation[0])
                elif rightIndex is None:  # 右边的是None，就把右边加到左边对应的组
                    equalSetList[leftIndex].add(equation[-1])
                else:  # 两个变量正常，已经存进去了
                    pass
            elif equation[1:3] == '!=':  # 处理不等于的情况
                if equation[0] == equation[-1]:  # 自己一定等于自己
                    return False
                leftIndex, rightIndex = None, None
                for i, equalSet in enumerate(equalSetList):
                    if equation[0] in equalSet:
                        leftIndex = i
                    if equation[-1] in equalSet:
                        rightIndex = i
                if leftIndex is not None and rightIndex is not None and leftIndex == rightIndex:  # 两个都不是None，比较所在的组号
                    return False
                elif leftIndex is None and rightIndex is None:  # 两个都是None，新建两个新组，分别放这两个
                    equalSetList += [{equation[0]}, {equation[-1]}]
                    continue
                elif leftIndex is None:  # 左边的是None，就新建一个组把左边的放进去
                    equalSetList += [{equation[0]}]
                elif rightIndex is None:  # 右边的是None，就新建一个组把右边的放进去
                    equalSetList += [{equation[-1]}]
                else:
                    pass
            else:
                raise ValueError("只支持包含'=='或'!='的式子")
        return True


print(Solution().equationsPossible(["a==b", "b!=a"]))
print(Solution().equationsPossible(["b==a", "a==b"]))
print(Solution().equationsPossible(["a==b", "b==c", "a==c"]))
print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))
print(Solution().equationsPossible(["c==c", "b==d", "x!=z"]))
print(Solution().equationsPossible(["a!=a"]))
print(Solution().equationsPossible(["b!=c", "a==b", "e!=d", "b!=f", "a!=b"]))
print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))
print(Solution().equationsPossible(["c==c", "f!=a", "f==b", "b==c"]))
print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))
print(Solution().equationsPossible(["b!=f", "c!=e", "f==f", "d==f", "b==f", "a==f"]))
print(Solution().equationsPossible(["i!=c", "i!=f", "k==j", "g==e", "h!=e", "h==d", "j==e", "k==a", "i==h"]))
