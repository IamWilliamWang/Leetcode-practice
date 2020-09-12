# string = input().strip()
# n = int(input().strip())
# result = '9' * len(string)
# nowStr = ''
#
#
# def dfs(i: int, eraser: int):
#     global result, nowStr
#     if i == len(string):
#         result = min(result, nowStr)
#         return
#     if eraser == 0:
#         result = min(result, nowStr + string[i:])
#         return
#     nowStr += string[i]
#     dfs(i + 1, eraser)
#     nowStr = nowStr[:-1]
#     if eraser > 0:
#         dfs(i + 1, eraser - 1)
#
#
# dfs(0, n)
# print(int(result))

# string = input().strip()
# n = int(input().strip())
# for _ in range(n):
#     prev = '0'
#     deleteIdx = -1
#     for i, ch in enumerate(string):
#         if ch < prev:
#             deleteIdx = i - 1
#             break
#         prev = ch
#     else:
#         deleteIdx = len(string) - 1
#     string = string[:deleteIdx] + string[deleteIdx + 1:]
# print(int(string))

string = input().strip()
n = int(input().strip())
prev = '0'
i = 0
while n:
    if i >= len(string):
        string = string[:-n]
        break
    ch = string[i]
    if ch < prev:
        deleteIdx = i - 1
        string = string[:deleteIdx] + string[deleteIdx + 1:]
        n -= 1
        continue
    prev = string[i]
    i += 1
print(int(string))
