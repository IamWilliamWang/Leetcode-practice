from typing import List
from collections import defaultdict, OrderedDict
from functools import lru_cache
from test_script import deprecated


class Solution:
    @deprecated
    def findOrder_no_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        @lru_cache(maxsize=None)
        def bfs(startNum: int) -> List[int]:
            queue: [List[int]] = [startNum]
            visited: [List[int]] = []
            while queue:
                now = queue.pop(0)
                if now in visited:
                    return []
                visited.append(now)
                if now in adjGraph:
                    queue += adjGraph[now]
            return visited

        def cast(bfsResult: List[int]):
            return sorted(independentCourses, key=lambda num: -num) + list(reversed(bfsResult))

        adjGraph = defaultdict(list)
        nonIndependentCourses = set()
        for key, value in prerequisites:
            adjGraph[key].append(value)
            nonIndependentCourses.add(key)
            nonIndependentCourses.add(value)
        independentCourses = list(set(range(numCourses)).difference(nonIndependentCourses))
        for key in adjGraph:
            bfsResult = bfs(key)
            if len(bfsResult) == numCourses - len(independentCourses):
                return cast(bfsResult)
        if not prerequisites:
            return list(range(numCourses - 1, -1, -1))
        return []

    @deprecated
    def existCircle(self, 邻接表: dict) -> bool:
        for key in 邻接表:
            for value in 邻接表[key]:
                if value not in 邻接表:
                    return True
        return False

    def find入度为0的节点(self, 邻接表: dict) -> List[int]:
        # if self.existCircle(邻接表):
        #     return []
        入度为零List: List[int] = []
        keys: List[int] = list(邻接表.keys())
        for nowNodeIndex in range(len(keys)):
            nowNode = keys[nowNodeIndex]
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

    @deprecated
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites.sort()
        adjustMap = {}
        # 生成邻接表
        for key, value in prerequisites:
            adjustMap.setdefault(key, []).append(value)
        for i in range(numCourses):
            adjustMap.setdefault(i, [])
        # 开始拓扑排序
        visited = []
        while len(adjustMap) != 0:
            入度为0的节点List = self.find入度为0的节点(adjustMap)
            if not 入度为0的节点List:
                return []
            for 入度为零的节点 in 入度为0的节点List:
                visited.append(入度为零的节点)
                del adjustMap[入度为零的节点]
        return list(reversed(visited))

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            nextNodes = adjustMap[node]
            for nextNode in nextNodes:
                if not dfs(nextNode):
                    return False
            if node not in result:
                result.append(node)
            visited.remove(node)
            return True

        adjustMap = defaultdict(list)
        visited = set()
        result = []
        for key, value in prerequisites:
            adjustMap[key].append(value)
        for i in range(numCourses-1, -1, -1):
            adjustMap.setdefault(i, [])
        tmp = self.find入度为0的节点(adjustMap)
        dfsWithoutCircle = [dfs(node) for node in tmp]
        if False in dfsWithoutCircle:
            return []
        return result


print(Solution().findOrder2(3, [[1,0],[2,0]]))
