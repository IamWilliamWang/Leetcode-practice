import sys
n,m=list(map(int,sys.stdin.readline().strip().split()))
c,w=[],[]
credits=[]
for i in range(n):
    ci,wi=list(map(int,sys.stdin.readline().strip().split()))
    c.append(ci)
    w.append(wi)
restBlood=0
restMoney=0
for i in range(n):
    while restBlood < c[i]:
        restBlood+=m
        restMoney-=1
    restBlood-=c[i]
    restMoney+=w[i]
    credits.append(restMoney)
result=max(credits)
print(result if result >0 else 0)