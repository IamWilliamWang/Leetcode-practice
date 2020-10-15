counter = {}
inputString = input().strip()
for ch in inputString:
    counter[ch] = counter.setdefault(ch, 0) + 1
minTimes = min(counter.values())
for ch in inputString:
    if counter[ch] > minTimes:
        print(ch, end='')
