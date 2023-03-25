# https://codeforces.com/gym/430380/problem/E

n, k = map(int, input().split())
ratings = list(map(int, input().split()))


def conquer(left_side, right_side, merged):
    left_ptr, right_ptr = 0, 0
    left_min, right_min = ratings[left_side[0]], ratings[right_side[0]]

    while left_ptr < len(left_side) and right_ptr < len(right_side):
        if ratings[left_side[left_ptr]] <= ratings[right_side[right_ptr]]:
            if right_min - ratings[left_side[left_ptr]] <= k:
                merged.append(left_side[left_ptr])
            left_ptr += 1
        else:
            if left_min - ratings[right_side[right_ptr]] <= k:
                merged.append(right_side[right_ptr])
            right_ptr += 1

    while left_ptr < len(left_side) and right_min - ratings[left_side[left_ptr]] <= k:
        merged.append(left_side[left_ptr])
        left_ptr += 1

    while right_ptr < len(right_side) and left_min - ratings[right_side[right_ptr]] <= k:
        merged.append(right_side[right_ptr])
        right_ptr += 1


def divide(i, total_players, k):
    if total_players == 1:
        return [i]

    left_side = divide(i, total_players // 2, k)
    right_side = divide(i + (total_players // 2), total_players // 2, k)

    merged = []
    conquer(left_side, right_side, merged)

    return merged


merged = divide(0, 2**n, k)
merged.sort()

for i in range(len(merged)):
    merged[i] += 1

print(*merged)
