from collections import defaultdict

strCount, K = list(map(int, input().strip().split()))
strings = []
counter = defaultdict(int)
for _ in range(strCount):
    strings.append(input().strip())
    counter[strings[-1]] += 1
counterList = list(counter.items())
counterList.sort(key=lambda t: (-t[1], t[0]))
for tpl in counterList[:K]:
    print(*tpl)
counterList.sort(key=lambda t: (t[1], t[0]))
for tpl in counterList[:K]:
    print(*tpl)
