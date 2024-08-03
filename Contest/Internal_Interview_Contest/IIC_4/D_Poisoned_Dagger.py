def has_enough_damage(hit, attack_time, target_damage, n):
    total_damage = hit  # For the last attack time reserve one hit
    for i in range(n-1):
        total_damage += min(hit, attack_time[i+1] - attack_time[i])

    return total_damage >= target_damage


def solve():
    t = int(input())
    for _ in range(t):
        n, target_damage = map(int, input().split())
        attack_time = list(map(int, input().split()))

        L, R = 1, target_damage

        while L < R:
            mid = L + (R - L) // 2
            if has_enough_damage(mid, attack_time, target_damage, n):
                R = mid
            else:
                L = mid + 1

        print(L)


solve()
