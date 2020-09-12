from itertools import chain


def main():
    cowCount, needSectionCount = list(map(int, input().strip().split()))
    sections所有 = []
    for _ in range(needSectionCount):
        sections本品质 = []
        for _ in range(int(input().strip())):
            sections本品质.append(tuple(map(int, input().strip().split())))
        sections所有.append(sections本品质)
    orders = []
    for tmp in sections所有:
        for sectionTpl in tmp:
            begin, end = sectionTpl
            orders += [(begin, True), (end, False)]  # 时间点，是否打开区间
    orders.sort(key=lambda x: (x[0], not x[1]))
    same = 0
    goodSections = []
    sectionStart, sectionEnd = -1, -1
    for orderTime, orderType in orders:
        if orderType:  # 打开
            same += 1
            if same == needSectionCount:
                sectionStart = orderTime
        else:
            sectionEnd = orderTime
            if same == needSectionCount:
                goodSections += [(sectionStart, sectionEnd)]
            same -= 1
    print(sum((end + 1 - begin for begin, end in goodSections)))
    allRanges = (range(begin, end + 1) for begin, end in goodSections)
    print(' '.join(map(str, chain(*allRanges))))


for _ in range(int(input().strip())):
    main()
