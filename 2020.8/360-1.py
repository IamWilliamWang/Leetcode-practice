CHARS对称 = set('AHIMOTUVWXY')
while True:
    inStr = input().strip()
    if inStr != inStr[::-1]:
        print('NO')
        continue
    if len([ch for ch in inStr if ch in CHARS对称]) == len(inStr):
        print('YES')
    else:
        print('NO')
