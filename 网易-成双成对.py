from collections import defaultdict

string = input().strip()
result = 0
for start in range(len(string)):
    counter = defaultdict(int)
    end = 0
    for end in range(start, len(string)):
        if string[end] not in 'abcxyz':
            continue
        counter[string[end]] += 1
        if all([x % 2 == 0 for x in counter.values()]):
            result = max(result, end - start + 1)
    if all([x % 2 == 0 for x in counter.values()]):
        result = max(result, end - start + 1)
print(result)
# maxLen = 0
# maxI, maxJ = -1, -1
# i, j = 0, 0
# counter = defaultdict(int)
# while j < len(string):
#     while all([x % 2 == 0 for x in counter.values()]):
#         if string[j] in 'abcxyz':
#             counter[string[j]] += 1
#         j += 1
#     if j - i > maxLen:
#         maxLen = j - i
#         maxI, maxJ = i, j
#     counter[string[i]] -= 1
#     i += 1
# print(maxLen)
