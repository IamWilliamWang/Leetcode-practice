class Solution:
    def isConvex(self, points: list) -> bool:
        import numpy as np
        crossedResults = []
        for i in range(len(points)):
            vertex1 = [points[i + 1 - len(points)][0] - points[i][0], points[i + 1 - len(points)][1] - points[i][1]]
            vertex2 = [points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1]]
            crossedResult = np.cross(vertex1, vertex2)
            crossedResults += [crossedResult.tolist()]
        crossedResults = np.array(crossedResults)
        return np.all(crossedResults >= 0) or np.all(crossedResults <= 0)


print(Solution().isConvex([[0,0],[1,0],[1,1],[-1,1],[-1,0]]))
