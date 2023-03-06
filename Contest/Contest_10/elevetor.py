# https://codeforces.com/gym/430380/problem/C

test_cases = int(input())

for _ in range(test_cases):
    walk_time, elev_time, elev_floor = map(int, input().split())
    matching_time = min(2 * elev_time * elev_floor, walk_time * elev_floor)

    print(matching_time + (4 - elev_floor) * min(walk_time, elev_time))
