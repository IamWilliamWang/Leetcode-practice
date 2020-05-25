import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    inputs=[]
    for _ in range(n):
        x,y= list(map(int, sys.stdin.readline().strip().split()))
        inputs+=[(x,y)]
    circles=[]
    for line in inputs:
        found=False
        for circle in circles:
            if line[0] in circle:
                circle.append(line[1])
                found=True
                break
            elif line[1] in circle:
                circle.append(line[0])
                found=True
                break
        if found:
            break
        if not found:
            circles.append(list(line))
    print(len(circles))