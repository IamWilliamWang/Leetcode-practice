import sys
n,k=list(map(int,sys.stdin.readline().strip().split()))
things=[]
for _ in range(n):
    line=list(map(int,sys.stdin.readline().strip().split()))
    things.append(line)
def perfact(i,j):
    ans = True
    for index in range(1,k):
        if things[i][index]+things[j][index]==things[i][index-1]+things[j][index-1]:
            continue
        ans=False
        break
    return ans
result=0
for i in range(n):
    for j in range(i+1,n):
        if perfact(i,j):
            result+=1
print(result)