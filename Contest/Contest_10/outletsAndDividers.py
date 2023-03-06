# https://codeforces.com/gym/430380/problem/B

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    dividers = list(map(int, input().split()))
    dividers.sort(reverse=True)

    slots = 2
    count = 0

    if n <= slots:
        print(count)
        continue

    for new_slot in dividers:
        slots += new_slot - 1
        count += 1

        if slots >= n:
            print(count)
            break

    if slots >= n:
        continue

    print(-1)

