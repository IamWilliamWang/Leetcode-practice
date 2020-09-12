import re

N = int(input().strip())
for _ in range(N):
    inputStr = input().strip()
    if not re.findall(r'^[a-zA-Z][a-zA-Z0-9]+$', inputStr):
        print('Wrong')
        continue
    if not [ch for ch in inputStr if ch.isdigit()]:
        print('Wrong')
        continue
    print('Accept')
