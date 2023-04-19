# https://codeforces.com/problemset/problem/1033/A

n = int(input())
queen = list(map(int, input().split()))
king = list(map(int, input().split()))
target = list(map(int, input().split()))


def is_attacked(x, y):
    if x == queen[0] or y == queen[1] or x + y == queen[0] + queen[1] \
            or x - y == queen[0] - queen[1]:
        return True

    return False

def in_same_quadrant():
    if (king[0] - queen[0]) * (target[0] - queen[0]) > 0 \
            and (king[1] - queen[1]) * (target[1] - queen[1]) > 0:
        return True

    return False


if not is_attacked(king[0], king[1]) and \
        not is_attacked(target[0], target[1]) \
        and in_same_quadrant():
    print("YES")
else:
    print("NO")
