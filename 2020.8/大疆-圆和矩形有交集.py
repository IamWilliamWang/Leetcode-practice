from math import sqrt
import sys


def _print(s):
    sys.stdout.write(s)


def main():
    r, r_x, r_y, xmin, ymin, xmax, ymax = list(map(int, input().strip().split()))

    # detect inside - 判断圆心在不在矩形内
    if xmin <= r_x <= xmax and ymin <= r_y <= ymax:
        _print('True')
        return
    # detect left - 解直线与圆的方程，然后看交点是否合理
    delta = r ** 2 - (xmin - r_x) ** 2
    if delta >= 0:
        y = [r_y + sqrt(delta), r_y - sqrt(delta)]
        for tmp in y:
            if ymin <= tmp <= ymax:
                _print('True')
                return
    # detect right
    delta = r ** 2 - (xmax - r_x) ** 2
    if delta >= 0:
        y = [r_y + sqrt(delta), r_y - sqrt(delta)]
        for tmp in y:
            if ymin <= tmp <= ymax:
                _print('True')
                return
    # detect top
    delta = r ** 2 - (ymin - r_y) ** 2
    if delta >= 0:
        x = [r_x + sqrt(delta), r_x - sqrt(delta)]
        for tmp in x:
            if xmin <= tmp <= xmax:
                _print('True')
                return
    # detect bottom
    delta = r ** 2 - (ymax - r_y) ** 2
    if delta >= 0:
        x = [r_x + sqrt(delta), r_x - sqrt(delta)]
        for tmp in x:
            if xmin <= tmp <= xmax:
                _print('True')
                return
    _print('False')


if __name__ == '__main__':
    main()

# 1 0 0 1 -1 3 1 True
# 1 0 0 -1 0 0 1 True
# 1 1 1 -3 -3 3 3 True
# 1 1 1 1 -3 2 -1 False
