#
# 现在给定所有的城市和航班，以及出发城市src，你的任务是找到从 scr城市出发到其他所有城市最便宜的机票价格列表。  假设两个城市之间机票价格不会超过Integer.MAX_V
# @param n int整型
# @param flights int整型二维数组
# @param src int整型
# @return int整型一维数组
#
from collections import defaultdict
from typing import List


class Solution:
    def findAllCheapestPrice(self, n: int, flights: List[List[int]], src: int) -> List[int]:
        edges = defaultdict(list)
        for flight in flights:
            edges[flight[0]].append(tuple(flight[1:]))
        costs = [2 ** 31 - 1] * n
        visited = set()

        def next():
            minCostNode, minCost = None, 2 ** 31 - 1
            for node, cost in enumerate(costs):
                if node in visited:
                    continue
                if cost < minCost:
                    minCost = cost
                    minCostNode = node
            return minCostNode, minCost

        def dijkstra(rootNode: int):
            costs[rootNode] = 0
            visited.add(rootNode)
            for edge in edges[rootNode]:
                costs[edge[0]] = edge[1]
            while True:
                node, cost = next()
                if not node:
                    break
                visited.add(node)
                adjNodes = edges[node]
                for adjNode, edgeCost in adjNodes:
                    new_cost = cost + edgeCost
                    if new_cost < costs[adjNode]:
                        costs[adjNode] = new_cost

        dijkstra(src)
        return [cost if cost != 2 ** 31 - 1 else -1 for cost in costs]


print(Solution().findAllCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0))
print(Solution().findAllCheapestPrice(5, [[0, 1, 10], [0, 3, 40], [1, 2, 20], [1, 3, 100], [1, 4, 30], [2, 3, 50],
                                          [3, 4, 60]], 1))
