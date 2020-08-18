import math
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    center: Point
    radius: float


@dataclass
class OBB:
    center: Point
    width: float
    height: float
    angleInRadian: float


def isCross_slow(circle: Circle, obb: OBB) -> bool:
    def distance(A, B, C):  # 点到直线距离公式，x0、y0代入圆的中心点
        return abs(A * circleX + B * circleY + C) / math.sqrt(A ** 2 + B ** 2)

    width, height, centerPointX, centerPointY, angle = obb.width, obb.height, obb.center.x, obb.center.y, obb.angleInRadian
    circleX, circleY, radius, = circle.center.x, circle.center.y, circle.radius
    # 判断上面
    uplineCenterX = centerPointX - height / 2 * math.sin(angle)
    uplineCenterY = centerPointY + height / 2 * math.cos(angle)
    k_up = math.tan(angle)
    A, B, C = k_up, -1, -k_up * uplineCenterX + uplineCenterY
    if distance(A, B, C) <= radius:  # 距离小于等于圆半径证明相交
        return True
    # 判断下面
    downlineCenterX = centerPointX * 2 - uplineCenterX
    downlineCenterY = centerPointY * 2 - uplineCenterY
    k_down = k_up
    A, B, C = k_down, -1, -k_down * downlineCenterX + downlineCenterY
    if distance(A, B, C) <= radius:
        return True
    # 判断左面
    leftlineCenterX = centerPointX - height / 2 * math.sin(angle + math.pi / 2)
    leftlineCenterY = centerPointY + height / 2 * math.cos(angle + math.pi / 2)
    k_left = math.tan(angle + math.pi / 2)
    A, B, C = k_left, -1, -k_left * downlineCenterX + downlineCenterY
    if distance(A, B, C) <= radius:
        return True
    # 判断右面
    rightlineCenterX = centerPointX * 2 - leftlineCenterX
    rightlineCenterY = centerPointY * 2 - leftlineCenterY
    k_right = k_left
    A, B, C = k_right, -1, -k_right * downlineCenterX + downlineCenterY
    if distance(A, B, C) <= radius:
        return True
    return False


@dataclass
class Line:
    K: float
    A: float
    B: float
    C: float
    centerX: float
    centerY: float
    length: float


def isCross(circle: Circle, obb: OBB) -> bool:
    def commonPoints(circle: Circle, line: Line) -> tuple:
        """
        求圆和直线的两个交点（可能重合），如果没有交点则返回None, None
        """
        x0, y0, r0, = circle.center.x, circle.center.y, circle.radius
        delta = (-2 * x0 + 2 * line.A * line.C / line.B) ** 2 + 4 * (1 + line.A ** 2 / line.B ** 2) * (
                r0 ** 2 - 2 * line.C * y0 / line.B - x0 ** 2 - y0 ** 2 - line.C ** 2)
        if delta < 0:
            return None, None  # 没有交点
        # 使用求根公式x=(-B+sqrt(delta))/2A and (-B-sqrt(delta))/2A
        point1X = ((2 * x0 - 2 * line.A * line.C / line.B - 2 * line.A * y0 / line.B) + math.sqrt(delta)) / (
                2 * (1 + line.A ** 2 / line.B ** 2))
        point2X = ((2 * x0 - 2 * line.A * line.C / line.B - 2 * line.A * y0 / line.B) - math.sqrt(delta)) / (
                2 * (1 + line.A ** 2 / line.B ** 2))
        point1Y = line.K * (point1X - line.centerX) + line.centerY  # y=k(x-x0)+y0
        point2Y = line.K * (point2X - line.centerX) + line.centerY
        return (point1X, point1Y), (point2X, point2Y)  # 返回两个交点的坐标

    def pointPointDistance(point1: tuple, point2: tuple):
        """
        两点距离
        """
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)  # (x1-x2)**2+(y1-y2)**2

    def isCrossLineCircle(K, lineCenterX, lineCenterY, length):
        line = Line(K, A, B, C, lineCenterX, lineCenterY, length)
        commonPoint1, commonPoint2 = commonPoints(circle, line)
        if commonPoint1 and commonPoint2:  # 有交点的时候
            # 如果交点和线段中点的距离小于等于线段长度的一半
            if pointPointDistance(commonPoint1, (uplineCenterX, uplineCenterY)) <= line.length / 2:
                return True
            if commonPoint1 != commonPoint2:
                if pointPointDistance(commonPoint2, (uplineCenterX, uplineCenterY)) <= line.length / 2:
                    return True
        return False

    width, height, centerPointX, centerPointY, angle = obb.width, obb.height, obb.center.x, obb.center.y, obb.angleInRadian
    # 判断上面
    uplineCenterX = centerPointX - height / 2 * math.sin(angle)
    uplineCenterY = centerPointY + height / 2 * math.cos(angle)
    k_up = math.tan(angle)
    A, B, C = k_up, -1, -k_up * uplineCenterX + uplineCenterY
    if isCrossLineCircle(k_up, uplineCenterX, uplineCenterY, width):
        return True
    # 判断下面
    downlineCenterX = centerPointX * 2 - uplineCenterX
    downlineCenterY = centerPointY * 2 - uplineCenterY
    k_down = k_up
    A, B, C = k_down, -1, -k_down * downlineCenterX + downlineCenterY
    if isCrossLineCircle(k_down, downlineCenterX, downlineCenterY, width):
        return True
    # 判断左面
    leftlineCenterX = centerPointX - height / 2 * math.sin(angle + math.pi / 2)
    leftlineCenterY = centerPointY + height / 2 * math.cos(angle + math.pi / 2)
    k_left = math.tan(angle + math.pi / 2)
    A, B, C = k_left, -1, -k_left * downlineCenterX + downlineCenterY
    if isCrossLineCircle(k_left, leftlineCenterX, leftlineCenterY, height):
        return True
    # 判断右面
    rightlineCenterX = centerPointX * 2 - leftlineCenterX
    rightlineCenterY = centerPointY * 2 - leftlineCenterY
    k_right = k_left
    A, B, C = k_right, -1, -k_right * rightlineCenterX + rightlineCenterY
    if isCrossLineCircle(k_right, rightlineCenterX, rightlineCenterY, height):
        return True
    return False
