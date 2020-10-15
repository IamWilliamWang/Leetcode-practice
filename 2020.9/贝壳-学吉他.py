import re

n = int(input().strip())
for _ in range(n):
    string = input().strip()
    print(len(re.findall('[4-6]3231323', string)))
