import sys
import bisect

n = int(input().strip())
arr = list(map(int, input().strip().split()))[:n]
# stackSortedOrder = []  # 守规矩的数字们（里面是顺序排列的）
# stackOthers = []  # 不守规矩的数字们
# for number in arr:
#     if not stackSortedOrder or stackSortedOrder[-1] < number:
#         stackSortedOrder.append(number)  # 守规矩就加进去
#     else:
#         # 发现栈顶是不守规矩的，踢出去
#         while stackSortedOrder and stackSortedOrder[-1] > number:
#             stackOthers.append(stackSortedOrder.pop())
#         stackSortedOrder.append(number)  # 加进去守规矩的这个数字
# # 本身插入这些不守规矩数字需要的次数
# ans = len(stackOthers)
# # 计算插入不守规矩数字时一共要挪动多少次守规矩的
# ans += len(stackSortedOrder) - bisect.bisect(stackSortedOrder, min(stackOthers))
# sys.stdout.write(str(ans))

# stack_to_right = []
# ans1 = 0
# for number in arr:
#     if stack_to_right and stack_to_right[-1] > number:
#         ans1 += 1
#     bisect.insort(stack_to_right, number)
# stack_to_left = []
# ans2 = 0
# for number in reversed(arr):
#     if stack_to_left and stack_to_left[0] < number:
#         ans2 += 1
#     bisect.insort(stack_to_left, number)
# sys.stdout.write(str(min(ans1, ans2)))
series = []
seriesLen = []
for number in arr:
    if number - 1 not in series:
        series.append(number)
        seriesLen.append(1)
    else:
        idx = series.index(number - 1)
        series[idx] = number
        seriesLen[idx] += 1
ans = n - max(seriesLen + [0])
sys.stdout.write(str(ans))
# seriesSortedOrder = []
# for number in arr:
#     idx = bisect.bisect(seriesSortedOrder, number)
#     if idx != len(seriesSortedOrder):
#         seriesSortedOrder[idx] = number
#     else:
#         seriesSortedOrder += [number]
# ans = n - len(seriesSortedOrder)
# sys.stdout.write(str(ans))
