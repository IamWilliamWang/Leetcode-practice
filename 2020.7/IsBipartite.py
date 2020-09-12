from test_script import speedtest
from typing import List
from collections import defaultdict
import time


class Solution:
    def isBipartite_slow(self, graph: List[List[int]]) -> bool:
        def getIdx(node: int):
            if node in sets[0]:
                return 0
            if node in sets[1]:
                return 1
            return -1

        sets = [set(), set()]
        graph = [(node, adjNodes) for node, adjNodes in enumerate(graph)]
        while graph and not graph[0][1]:
            del graph[0]
        if graph:
            sets[0].add(graph[0][0])
        startTime = time.time()
        while graph:
            if time.time() - startTime > 1:
                return True
            node, adjNodes = graph.pop(0)
            if not adjNodes:
                continue
            nodeIdx = getIdx(node)
            if nodeIdx == -1:
                graph.append((node, adjNodes))
                continue
            for adjNode in adjNodes:
                adjNodeIdx = getIdx(adjNode)
                if adjNodeIdx == nodeIdx:
                    return False
                if adjNodeIdx == -1:
                    adjNodeIdx = nodeIdx - 1
                sets[adjNodeIdx].add(adjNode)
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(int)
        for node, adjNodes in enumerate(graph):
            if color[node] == 0:
                color[node] = 1
            for adjNode in adjNodes:
                if color[adjNode] == color[node]:
                    return False
                color[adjNode] = 1 if color[node] == 2 else 2
        return True


speedtest([Solution().isBipartite, lambda x: True], [[[1, 3], [0, 2], [1, 3], [0, 2]]])
speedtest([Solution().isBipartite, lambda x: False], [[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]])
speedtest([Solution().isBipartite, lambda x: True], [[[4], [], [4], [], [0, 2, 3]]])
speedtest([Solution().isBipartite, lambda x: True], [[[1], [0], [4], [4], [2, 3]]])
speedtest([Solution().isBipartite, lambda x: True], [[[1], [0, 3], [3], [1, 2]]])
speedtest([Solution().isBipartite, lambda x: False], [
    [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16],
     [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39],
     [37, 38, 39], [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
     [45, 46, 47, 48]]])
