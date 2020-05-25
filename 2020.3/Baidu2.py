len=int(input().strip())
inputStr=input().strip()
matrix=[]
for i in range(len//2):
    row=[1]
    for j in range(i):
        row+=[0]
    matrix+=[row]
for j in len(matrix):
    for i in range(row):
        if i>0:
            row[i]=row[i-1]+3
for i in matrix[-1]:
    for i in range(row):
        if i>0:
            row[i]=row[i-1]+4
print(matrix[-1])



