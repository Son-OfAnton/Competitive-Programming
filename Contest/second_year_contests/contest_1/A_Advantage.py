from math import inf
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    first_strong, second_strong = -inf, -inf

    for num in arr:
        if num > first_strong:
            second_strong = first_strong
            first_strong = num
        elif num > second_strong:
            second_strong = num

    res = []
    for num in arr:
        if num == first_strong:
            res.append(num - second_strong)
        else:
            res.append(num - first_strong)

    print(*res)
