import sys
from functools import lru_cache
m,n=list(map(int,sys.stdin.readline().strip().split()))
result=0
@lru_cache(maxsize=None)
def getMatrix(i:int):
    if i==n-1:
        return [[x]for x in range(1,m+1)]
    result=[]
    subMatrix=getMatrix(i+1)
    for num in range(1,m+1):
        matrix = [m.copy() for m in subMatrix]
        for i in range(len(matrix)):
            matrix[i].insert(0, num)
        result += matrix
    return result
allSituations=getMatrix(0)
ans=0
for situation in allSituations:
    for i in range(1,len(situation)):
        if situation[i-1]==situation[i]:
            ans+=1
            break
print(ans)