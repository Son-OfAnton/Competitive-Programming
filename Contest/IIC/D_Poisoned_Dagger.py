def is_enough(hit, attack_time, target, n):
    total = 0
    for i, time in enumerate(attack_time):
        if i < n-1:
            if attack_time[i+1] - time < hit:
                total += attack_time[i+1] - time
            else:
                total += hit
        else:
            total += hit

    return total >= target

def solve():
    t = int(input())
    for _ in range(t):
        n, target = map(int, input().split())
        attack_time = list(map(int, input().split()))

        L, R = 1, 10**18

        while L < R:
            mid = L + (R - L) // 2
            if is_enough(mid, attack_time, target, n):
                R = mid
            else:
                L = mid + 1

        print(L)

solve()