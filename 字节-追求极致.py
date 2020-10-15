from collections import defaultdict

people, topN = list(map(int, input().strip().split()))
scores = defaultdict(int)
for _ in range(people):
    id, score = list(map(int, input().strip().split()))
    scores[id] += score
heap = list(scores.items())
heap.sort(key=lambda t: (-t[1], t[0]))
print(' '.join(map(str, (t[0] for t in heap[:topN]))))
