cols,rows,change=list(map(int,input().strip().split()))
fromStr=input()
toStr=input()
fromStatus = [int(ch) for ch in fromStr.replace('A','0').replace('B','1').replace('C','2')][:cols]
toStatus = [int(ch) for ch in toStr.replace('A','0').replace('B','1').replace('C','2')][:cols]
result = 0
def diff(status1,status2):
    ans = 0
    for id1,id2 in zip(status1,status2):
        ans+=abs(id1-id2)
    return ans
def dfs(depth:int):
    if depth>rows:
        return
    


print(result%1000000007)