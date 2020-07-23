from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edgesDict=defaultdict(list)
        for edge,confidence in zip(edges,succProb):
            edgesDict[edge[0]].append((edge[1],confidence))
            # edgesDict[edge[1]].append((edge[0],confidence))
        queue=[(start,1.0)]
        visited=set()
        maxConf=0
        while queue:
            startI,confidence=queue.pop(0)
            # if startI in visited:
            #     continue
            if startI==end:
                maxConf=max(maxConf,confidence)
            # visited.add(startI)
            for toI, edgeConf in edgesDict[startI]:
                queue+=[(toI,confidence*edgeConf)]
        return maxConf
        # paths=[]
        # visited=set()
        # def dfs(path:list,startI:int):
        #     if startI in visited:
        #         return
        #     visited.add(startI)
        #     if startI==end:
        #         paths.append(path)
        #         visited.remove(startI)
        #         return
        #     for toI,_ in edgesDict[startI]:
        #         dfs(path+[toI],toI)
        #     visited.remove(startI)
        # dfs([],start)
# print(Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))
print(Solution().maxProbability(5,[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],[0.37,0.17,0.93,0.23,0.39,0.04],3,4))
