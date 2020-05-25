import sys
n = int(sys.stdin.readline().strip())
A,B,C=list(map(int, sys.stdin.readline().strip().split()))
def x1(y):
    return 1/(2*A)*y*y
def x2(y):
    return 1/B*y-C/B
