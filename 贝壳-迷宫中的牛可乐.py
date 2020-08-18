from functools import lru_cache


def _input():
    import sys
    return sys.stdin.readline()
rows,cols=map(int,_input().strip().split())
map=[]
for _ in range(rows):
    map.append([ch for ch in _input().strip()])
nodeMap=[[0 for _ in range(rows*cols)] for _ in range(rows*cols)]
i,j=None,None
for i in range(rows):
    found=False
    for j in range(cols):
        if map[i][j]=='.':
            found=True
            break
    if found:
        break
def bfs(starti,startj):
    @lru_cache(maxsize=None)
    def canWalk(nowI,nowJ):
        if not (0<=nowI<rows) or not (0<=nowJ<cols):
            return False
        return map[nowI][nowJ]=='.'
    queue=[(starti,startj)]
    visited=set()
    while queue:
        i,j=queue.pop(0)
        if (i,j) in visited:
            continue
        visited.add((i,j))
        nextSteps=[(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if canWalk(x,y)]
        for x,y in nextSteps:
            nodeMap[i * rows + j][x * rows + y]=nodeMap[x * rows + y][i * rows + j]=1
        queue+=nextSteps
generateNodeMap=bfs(i,j)
class Floyd_Path():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        for k in range(self.node_length):
            for i in range(self.node_length):
                for j in range(self.node_length):
                    tmp = self.node_map[i][k] + self.node_map[k][j]
                    if self.node_map[i][j] > tmp:
                        self.node_map[i][j] = tmp
floyd=Floyd_Path(nodeMap)
print(max(floyd.node_map))

