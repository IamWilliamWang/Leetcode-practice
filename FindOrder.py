# 继续写完FindOrderDeprecated类，之前的没通过测试
from typing import List
from collections import defaultdict

from test_script import speedtest, standard


class Solution:
    def find入度为0的节点(self, 邻接表: dict) -> List[int]:
        入度为零List: List[int] = []
        keys: List[int] = list(邻接表.keys())
        for nowNodeIndex, nowNode in enumerate(keys):
            当前入度为0: bool = True
            for otherNodeIndex in range(len(keys)):
                if nowNodeIndex == otherNodeIndex:
                    continue
                otherNode = keys[otherNodeIndex]
                if nowNode in 邻接表[otherNode]:  # 如果发现其他节点存在指向当前节点的
                    当前入度为0 = False
                    break
            if 当前入度为0:
                入度为零List.append(nowNode)
        return 入度为零List

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for nextNode in adjustMap[node]:
                if not dfs(nextNode):
                    success = False
                    break
            else:
                success = True
                if node not in result:
                    result.append(node)
            visited.remove(node)
            return success

        adjustMap = defaultdict(list)
        visited = set()
        result = []
        # 换成邻接表
        for key, value in prerequisites:
            adjustMap[key].append(value)
        dfsWithoutCircle = [dfs(node) for node in self.find入度为0的节点(adjustMap)]
        if False in dfsWithoutCircle:
            return []
        return result


speedtest(standard(Solution().findOrder, [0, 1]), (2, [[1, 0]]), False)
speedtest(standard(Solution().findOrder, [0, 1, 2, 3]), (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), False)  # or [0,2,1,3]
speedtest(standard(Solution().findOrder, []), (8, [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]), False)
speedtest(standard(Solution().findOrder, [0, 1, 2]), (3, [[1, 0], [2, 1]]), False)
speedtest(standard(Solution().findOrder, []), (2, [[1, 0], [0, 1]]), False)
speedtest(standard(Solution().findOrder, [0, 2, 1]), (3, [[1, 0], [2, 0]]), False)
speedtest(standard(Solution().findOrder, [2, 0, 1]), (3, [[1, 0]]), False)
speedtest(standard(Solution().findOrder, []), (2, [[0, 1], [1, 0]]), False)
speedtest(standard(Solution().findOrder, [0, 1]), (2, [[1, 0]]), False)
speedtest(standard(Solution().findOrder, [0, 1]), (2, [[1, 0]]), False)
